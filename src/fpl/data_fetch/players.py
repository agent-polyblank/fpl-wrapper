"""Information relating to actual players."""

import json

import httpx

from fpl.model.players_models import PlayerData, PlayerDetail


def get_all_player_detail(
    client: httpx.Client,
) -> list[PlayerDetail]:
    """
    Get all player details from the FPL API.

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


def get_player_summary(client: httpx.Client, player_id: str) -> httpx.Response:
    """
    Get player summary from the FPL API.

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


def get_player_by_id(
    client: httpx.Client,
    player_id: int,
    get_player_summary_func: callable,
    get_all_player_detail_func: callable,
) -> PlayerData:
    """
    Get player data by player id.

    Args:
    ----
        client (httpx.Client): httpx client instance.
        player_id (int): player id.
        get_player_summary_func (callable): get_player_summary function.
        get_all_player_detail_func (callable): get_all_player_detail function.

    Returns:
    -------
        PlayerData: PlayerData object.

    """
    player_summary = get_player_summary_func(client, player_id)
    all_player_details = get_all_player_detail_func(client)

    return PlayerData(
        player_detail=all_player_details[player_id - 1],
        **player_summary.json(),
    )
