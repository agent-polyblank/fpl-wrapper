"""Information relating to actual players."""

import httpx

from fpl_wrapper.model.players_models import PlayerData, PlayerDetail


def get_players(data: dict[str, any]) -> dict[int, PlayerDetail]:
    """
    Get all players in league.

    Args:
    ----
        data (dict[str, any]): league data.

    Returns:
    -------
        list[PlayerDetail]: Details of all players in the league.

    """
    return {player["id"]: PlayerDetail(**player) for player in data["elements"]}


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
    bootstrap_data: list[PlayerDetail],
) -> PlayerData:
    """
    Get player data by player id.

    Args:
    ----
        client (httpx.Client): httpx client instance.
        player_id (int): player id.
        bootstrap_data(list[PlayerDetail]): List of player details.

    Returns:
    -------
        PlayerData: PlayerData object.

    """
    player_summary = get_player_summary(client, player_id)

    return PlayerData(
        player_detail=bootstrap_data[player_id],
        **player_summary.json(),
    )
