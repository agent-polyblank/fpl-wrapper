"""Analysis of FPL data."""

import httpx

from fpl.data_fetch.managers import get_manager_gw_data
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
    player_picks: list[ManagerTeamData] = [
        get_manager_gw_data(httpx.client(), player_id, i)
        for i in range(gameweek_from, gameweek_to)
    ]

    _ = count_player_picks(player_picks, formation)
