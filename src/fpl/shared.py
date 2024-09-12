"""Shared functions for the FPL API."""

import json

import httpx

from fpl.models import PlayerData, PlayerDetail


def get_static_content() -> dict:
    """Get all the static content from the FPL API.

    Returns
    -------
        dict: Static content from the FPL API.

    """
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    return json.loads(httpx.get(url, headers={}, data={}).text)


def get_all_player_detail(data: dict[str:any]) -> list[PlayerDetail]:
    """Get all player details from the FPL API.

    Returns
    -------
        list[PlayerDetail]: List of player details.

    """
    return [PlayerDetail(**player) for player in data["elements"]]


def get_picks(team_id: str, gw: str) -> list[dict]:
    """Get player picks for a specific gameweek.

    Args:
    ----
        team_id (str): Player's team id.
        gw (str): Gameweek number.

    Returns:
    -------
        list[dict]: list of player picks for a specific gameweek.

    """
    url = f"https://fantasy.premierleague.com/api/entry/{team_id}/event/{gw}/picks/"
    return json.loads(httpx.get(url, headers={}, data={}).text)["picks"]


def get_player_by_id(player_id: str) -> PlayerData:
    """Get player data from the FPL API.

    Args:
    ----
        player_id (str): Player id.

    Returns:
    -------
        PlayerData: Player data.

    """
    url = f"https://fantasy.premierleague.com/api/element-summary/{player_id}/"
    response = httpx.get(url)
    player_data = response.json()
    return PlayerData(**player_data)
