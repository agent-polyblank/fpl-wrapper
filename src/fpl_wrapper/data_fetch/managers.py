"""Endpoints relating to fpl managers."""

import httpx

from fpl_wrapper.model.manager_basic import ManagerBase
from fpl_wrapper.model.managers_models import LeagueData, ManagerTeamData


class Managers:
    """
    Class to fetch manager data from the FPL API.

    Attributes
    ----------
        client (httpx.Client): HTTP client instance.

    """

    def __init__(
        self,
        client: httpx.Client,
    ) -> None:
        """Initialise Manager class."""
        self.client = client

    def get_league_data(self, league_id: str, page: int) -> LeagueData:
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
        return LeagueData(**self.client.get(url).json())

    def get_manager_gw_data(self, team_id: str, gw: str) -> ManagerTeamData:
        """
        Get manager data for a specific gameweek.

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
        return ManagerTeamData(**self.client.get(url).json())

    def get_manager_basic_info(self, manager_id: str) -> ManagerBase:
        """
        Get basic information about a manager.

        Args:
        ----
            client (httpx.Client): httpx client instance.
            manager_id (str): Manager id.

        Returns:
        -------
            ManagerBase: Manager details.

        """
        url = f"https://fantasy.premierleague.com/api/entry/{manager_id}/"
        return ManagerBase(**self.client.get(url).json())
