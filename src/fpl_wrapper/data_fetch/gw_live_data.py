"""Module for fetching live gw data."""

import httpx

from fpl_wrapper.model.gw_live_models import EventLiveResponse


class GWLiveData:
    """Class for fetching gw live data."""

    def __init__(self, client: httpx.Client) -> None:
        """
        Initialise GW live data fetcher.

        Args:
        ----
            client (httpx.Client): httpx client.

        """
        self.client = client

    def get_live_data(self, gameweek: int) -> EventLiveResponse:
        """
        Fetch live data.

        Args:
        ----
            gameweek (int): Gameweek number.

        Returns:
        -------
            LiveElement: Live event data.

        """
        url = f"https://fantasy.premierleague.com/api/event/{gameweek}/live/"
        response = self.client.get(url)
        return EventLiveResponse(**response.json())
