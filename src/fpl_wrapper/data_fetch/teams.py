"""Teams data fetcher module."""

import httpx

from fpl_wrapper.data_fetch.bootstrap_data import get_bootstrap_data
from fpl_wrapper.model.bootstrap_models import TeamData


class Teams:
    """Class to fetch and manage teams data."""

    def __init__(self, client: httpx.Client) -> None:
        """Initialise Teams class."""
        self.client = client
        self.bootstrap_data = get_bootstrap_data(client)
        self.teams = {team.id: team for team in self.bootstrap_data.teams}

    def get_team(self, team_id: int) -> dict[str, str]:
        """
        Get team data by team ID.

        Args:
        ----
            team_id (int): Team ID.

        Returns:
        -------
            dict[str, str]: Team data.

        """
        return self.teams[team_id]

    def get_teams(self) -> dict[int, TeamData]:
        """
        Get all teams data.

        Returns
        -------
            dict[int, dict[str, str]]: All teams data.

        """
        return self.teams
