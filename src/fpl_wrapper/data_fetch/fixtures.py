"""Data fetching functions for fixtures."""

import httpx

from fpl_wrapper.model.fixture_models import Fixtures


def get_fixtures(client: httpx.Client, gameweek: int, team_id: int) -> Fixtures:
    """
    Get fixtures.

    Args:
    ----
        client (httpx.Client): HTTP client instance.
        gameweek (int): Gameweek number.
        team_id (int): Team id.

    Returns:
    -------
        list[dict]: List of fixtures.

    """
    params = {}
    if gameweek:
        params["event"] = gameweek
    if team_id:
        params["team"] = team_id

    response = client.get(
        "https://fantasy.premierleague.com/api/fixtures/", params=params
    )
    return Fixtures(fixtures=response.json())
