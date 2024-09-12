"""Shared functions for the FPL API."""

import json

import httpx

from fpl.models import PlayerData, PlayerDetail


def get_all_player_detail(
    client: httpx.Client,
) -> list[PlayerDetail]:
    """Get all player details from the FPL API.

    Args:
    ----
        client (httpx.Client): HTTP client instance.
        data (dict[str, any]): Static content data.

    Returns:
    -------
        list[PlayerDetail]: List of player details.

    """
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    data = json.loads(client.get(url).text)
    return [PlayerDetail(**player) for player in data["elements"]]


def get_picks(client: httpx.Client, team_id: str, gw: str) -> list[dict]:
    """Get player picks for a specific gameweek.

    Args:
    ----
        client (httpx.Client): HTTP client instance.
        team_id (str): Player's team id.
        gw (str): Gameweek number.

    Returns
    -------
        list[dict]: list of player picks for a specific gameweek.

    """
    url = f"https://fantasy.premierleague.com/api/entry/{team_id}/event/{gw}/picks/"
    return json.loads(client.get(url).text)["picks"]


def get_player_summary(client: httpx.Client, player_id: str) -> httpx.Response:
    """Get player summary from the FPL API.

    Args:
    ----
        client (httpx.Client): HTTP client instance.
        player_id (str): Player id.

    Returns:
    -------
        httpx.Response: Response object containing player summary.

    """
    url = f"https://fantasy.premierleague.com/api/element-summary/{player_id}/"
    return client.get(url)


def get_player_by_id(client: httpx.Client, player_id: str) -> PlayerData:
    """Get player data from the FPL API.

    Args:
    ----
        client (httpx.Client): HTTP client instance.
        player_id (str): Player id.

    Returns:
    -------
        PlayerData: Player data.

    """
    player_summary = get_player_summary(client, player_id)
    return PlayerData(
        player_detail=get_all_player_detail(get_static_content())[
            player_id - 1
        ],
        **player_summary.json(),
    )
