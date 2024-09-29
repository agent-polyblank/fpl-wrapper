"""Endpoints relating to fpl managers."""

import httpx

from fpl.model.managers_models import LeagueData, TeamData


def get_league_data(
    client: httpx.Client, league_id: str, page: int
) -> LeagueData:
    """
    Get league data and standings. This data is paginated.

    Args:
    ----
        client (httpx.Client): HTTP client instance.
        league_id (str): League id.
        page (int): Page number.

    Returns:
    -------
        dict: League data.

    """
    url = f"https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/?page_new_entries=1&page_standings={page}&phase=1"
    return LeagueData.model_validate_json(client.get(url).text)


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
