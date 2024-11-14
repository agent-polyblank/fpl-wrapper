"""Analysis of FPL data."""

import httpx

from fpl.data_fetch.managers import get_manager_gw_data
from fpl.data_fetch.players import (
    get_player_by_id,
    get_players,
)
from fpl.model.data_analysis import PlayerCount
from fpl.model.managers_models import (
    Formation,
    ManagerTeamData,
    PlayerTeam,
)
from fpl.model.players_models import PlayerData, PositionEnum


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
        for pick in gameweek.picks:
            player_counts[pick.element] = player_counts.get(pick.element, 0) + 1
    return player_counts


def get_most_common_formation(
    player_id: int,
    gameweek_from: int,
    gameweek_to: int,
    bootstrap_data: dict,
) -> Formation:
    """
    Get the player's most common team formation for a given period.

    Args:
    ----
        player_id (int): Player ID.
        gameweek_from (int): Start gameweek.
        gameweek_to (int): End gameweek.
        bootstrap_data (dict): Static content data.

    Returns:
    -------
        Formation: Most common team formation over the specified gameweeks.

    """
    client = httpx.Client()
    player_picks: list[ManagerTeamData] = [
        get_manager_gw_data(client, player_id, gameweek)
        for gameweek in range(gameweek_from, gameweek_to + 1)
    ]
    bootstrap_data = get_players(bootstrap_data)

    formations = []

    for gameweek in player_picks:
        formation = Formation(
            attackers=0, midfielders=0, defenders=0, goalkeepers=0
        )
        for player in gameweek.picks[0:11]:
            player_detail = get_player_by_id(
                client, player.element, bootstrap_data
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
    player_id: int,
    gameweek_from: int,
    gameweek_to: int,
    formation: Formation,
    bootstrap_data: dict,
) -> list[PlayerData]:
    """
    Get the player's average team for a given period.

    Args:
    ----
        player_id (int): Player ID.
        gameweek_from (int): gameweek_from.
        gameweek_to (int): game week to.
        formation (Formation): Formation.
        bootstrap_data (dict): Static content data.

    Returns:
    -------
        list[PlayerData]: Average team.

    """
    client = httpx.Client()
    player_picks: list[ManagerTeamData] = [
        get_manager_gw_data(client, player_id, gameweek)
        for gameweek in range(gameweek_from, gameweek_to + 1)
    ]

    counts: PlayerCount = count_player_picks(player_picks)

    players_sorted = sort_player_by_count(counts)

    # get each player's details
    bootstrap_data = get_players(bootstrap_data)

    player_detail = [
        get_player_by_id(client, pid[0], bootstrap_data)
        for pid in players_sorted
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
            match player.player_detail.element_type:
                case PositionEnum.Goalkeeper:
                    player_team.Goalkeepers.append(player)
                case PositionEnum.Defender:
                    player_team.Defenders.append(player)
                case PositionEnum.Midfielder:
                    player_team.Midfielders.append(player)
                case PositionEnum.Forward:
                    player_team.Forwards.append(player)

    return player_team


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
