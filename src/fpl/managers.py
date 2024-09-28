"""Endpoints relating to fpl managers."""

import httpx

from fpl.model.managers_models import LeagueData, TeamData


def get_league_data(client: httpx.Client, league_id: str) -> LeagueData:
    """
    Get league data.

    Args:
    ----
        client (httpx.Client): HTTP client instance.
        league_id (str): League id.

    Returns:
    -------
        dict: League data.

    """
    url = f"https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/"
    response = client.get(url)
    return LeagueData.model_validate_json(response.text)


def get_manager_gw_data(
    client: httpx.Client, team_id: str, gw: str
) -> TeamData:
    """
    Get player picks for a specific gameweek.

    Args:
    ----
        client (httpx.Client): HTTP client instance.
        team_id (str): Player's team id.
        gw (str): Gameweek number.

    Returns:
    -------
        list[dict]: list of player picks for a specific gameweek.

    """
    url = f"https://fantasy.premierleague.com/api/entry/{team_id}/event/{gw}/picks/"
    return TeamData.model_validate_json(client.get(url).text)
