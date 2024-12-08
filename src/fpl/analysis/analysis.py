"""Analysis of FPL data."""

import httpx

from fpl.data_fetch.managers import get_manager_gw_data
from fpl.data_fetch.players import (
    get_player_by_id,
)
from fpl.model.data_analysis import GameweekRange, PlayerCount
from fpl.model.managers_models import (
    Formation,
    ManagerTeamData,
    PlayerTeam,
)
from fpl.model.players_models import PlayerData, PlayerDetail, PositionEnum


def count_player_picks(gw_picks: list[ManagerTeamData]) -> PlayerCount:
    """
    Count player picks.

    Args:
    ----
        gw_picks (list[ManagerData]): List of manager data.

    Returns:
    -------
        dict[int, int]: Dictionary of player counts.

    """
    player_counts = PlayerCount()
    for gameweek in gw_picks:
        for pick in gameweek.picks[0:11]:
            player_counts[pick.element] = player_counts.get(pick.element, 0) + 1
    return player_counts


def get_most_common_formation(
    player_picks: list[ManagerTeamData],
    player_data: dict[int, PlayerDetail],
    client: httpx.Client,
) -> Formation:
    """
    Get the player's most common team formation for a given period.

    Args:
    ----
        player_id (int): Player Id.
        gameweek_range (GameweekRange): Range of gameweeks.
        player_picks (dict[int, PlayerDetail]): List of player picks.
        player_data (dict[int:any]): Static player data.
        client (httpx.Client): httpx client.

    Returns:
    -------
        Formation: Average player formation for gameeweek range.

    """
    formations = []

    for gameweek in player_picks:
        formation = Formation(
            attackers=0, midfielders=0, defenders=0, goalkeepers=0
        )
        for player in gameweek.picks[0:11]:  # Only select the starting XI
            player_detail = get_player_by_id(
                client, player.element, player_data
            )
            position = player_detail.player_detail.element_type
            match position:
                case PositionEnum.Goalkeeper:
                    formation.goalkeepers += 1
                case PositionEnum.Defender:
                    formation.defenders += 1
                case PositionEnum.Midfielder:
                    formation.midfielders += 1
                case PositionEnum.Forward:
                    formation.attackers += 1
        formations.append(formation)
    return max(set(formations), key=formations.count)


def get_player_average_team(
    formation: Formation,
    player_data: dict[int, PlayerDetail],
    player_picks: list[ManagerTeamData],
    client: httpx.Client,
) -> PlayerTeam:
    """
    Get the player's average team for a given period.

    Args:
    ----
        formation (Formation): Formation.
        player_data (dict[int, PlayerDetail]): Static content data.
        client(httpx.Client): httpx client.
        player_picks(list[ManagerTeamData]): Player picks per gameweek.

    Returns:
    -------
        PlayerTeam: Average team for given period.

    """
    counts: PlayerCount = count_player_picks(player_picks)

    players_sorted = sort_player_by_count(counts)

    player_detail = [
        get_player_by_id(client, pid[0], player_data) for pid in players_sorted
    ]

    position_limits = {
        "Goalkeeper": formation.goalkeepers,
        "Defender": formation.defenders,
        "Midfielder": formation.midfielders,
        "Forward": formation.attackers,
    }

    position_counts = {
        "Goalkeeper": 0,
        "Defender": 0,
        "Midfielder": 0,
        "Forward": 0,
    }

    player_team = PlayerTeam()

    for player in player_detail:
        position = player.player_detail.position
        if position_counts[position] < position_limits[position]:
            position_counts[position] += 1
            match player.player_detail.element_type:
                case PositionEnum.Goalkeeper:
                    player_team.goalkeepers.append(player)
                case PositionEnum.Defender:
                    player_team.defenders.append(player)
                case PositionEnum.Midfielder:
                    player_team.midfielders.append(player)
                case PositionEnum.Forward:
                    player_team.forwards.append(player)

    return player_team


def get_player_picks(
    player_id: int, gameweek_range: GameweekRange, client: httpx.Client
) -> list[ManagerTeamData]:
    """
    Get player picks for gameweek range.

    Args:
    ----
        player_id (int): Player Id.
        gameweek_range (GameweekRange): Range of gameweeks to get picks for.
        client (httpx.Client): httpx client.

    Returns:
    -------
        list[ManagerTeamData]: All player picks in a given period.

    """
    return [
        get_manager_gw_data(client, player_id, gameweek)
        for gameweek in range(
            gameweek_range.gameweek_from, gameweek_range.gameweek_to
        )
    ]


def sort_player_by_count(counts: PlayerCount) -> list[PlayerData]:
    """
    Sort players by count.

    Args:
    ----
        counts (PlayerCount): Player ids and counts.

    Returns:
    -------
        list[PlayerData]: List of players sorted by count.

    """
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)
