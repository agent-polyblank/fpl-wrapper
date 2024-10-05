"""Analysis of FPL data."""

import httpx

from fpl.data_fetch.managers import get_manager_gw_data
from fpl.data_fetch.players import (
    get_bootstrap_data,
    get_player_by_id,
    get_players,
)
from fpl.model.data_analysis import PlayerCount
from fpl.model.managers_models import Formation, ManagerTeamData
from fpl.model.players_models import PlayerData

test_formation = Formation(
    attackers=3, midfielders=4, defenders=3, goalkeepers=1
)


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


def get_player_average_team(
    player_id: int, gameweek_from: int, gameweek_to: int, formation: Formation
) -> list[PlayerData]:
    """
    Get the player's average team for a given period.

    Args:
    ----
        player_id (int): Player ID.
        gameweek_from (int): gameweek_from.
        gameweek_to (int): game week to.
        formation (Formation): Formation.

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
    bootstrap_data = get_players(get_bootstrap_data(client))

    players_sorted = [
        get_player_by_id(client, pid[0], bootstrap_data)
        for pid in players_sorted
    ]
    team = []
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

    for player in players_sorted:
        position = player.player_detail.position
        if position_counts[position] < position_limits[position]:
            team.append(player)
            position_counts[position] += 1

    return team


def sort_player_by_count(counts: PlayerCount) -> list[PlayerData]:
    """Sort players by count."""
    return sorted(counts.items(), key=lambda x: x[1])
