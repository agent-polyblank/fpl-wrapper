"""Data fetching functions for fixtures."""

import httpx

from fpl_wrapper.model.fixture_models import MatchData


def get_fixtures(client: httpx.Client) -> list[MatchData]:
    """
    Get fixtures.

    Args:
    ----
        client (httpx.Client): HTTP client instance.

    Returns:
    -------
        list[dict]: List of fixtures.

    """
    url = "https://fantasy.premierleague.com/api/fixtures/"
    data = client.get(url).json()
    return [MatchData(**fixture) for fixture in data]
