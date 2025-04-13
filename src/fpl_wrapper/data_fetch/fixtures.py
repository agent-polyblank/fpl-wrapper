"""Data fetching functions for fixtures."""

import httpx

from fpl_wrapper.model.fixture_models import Fixtures


class FixtureProvider:
    """
    Class to fetch fixture data from the FPL API.

    Attributes
    ----------
        client (httpx.Client): HTTP client instance.
        bootstrap_data (dict[str, any]): League data.

    """

    def __init__(
        self,
        client: httpx.Client,
    ) -> None:
        """Initialise Fixture class."""
        self.client = client

    def get_fixtures(self, gameweek: int, team_id: int) -> Fixtures:
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

        response = self.client.get(
            "https://fantasy.premierleague.com/api/fixtures/", params=params
        )
        return Fixtures(fixtures=response.json())
