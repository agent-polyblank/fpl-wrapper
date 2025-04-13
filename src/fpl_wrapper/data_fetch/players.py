"""Information relating to actual players."""

import httpx

from fpl_wrapper.data_fetch.bootstrap_data import get_bootstrap_data
from fpl_wrapper.model.players_models import (
    PlayerData,
    PlayerDetail,
    PlayerSummaryResponse,
)


class Players:
    """
    Class to fetch player data from the FPL API.

    Attributes
    ----------
        client (httpx.Client): HTTP client instance.
        bootstrap_data (dict[str, any]): League data.

    """

    def __init__(
        self,
        client: httpx.Client,
    ) -> None:
        """Initialise Player class."""
        self.client = client
        self.bootstrap_data = get_bootstrap_data(client)

    def get_players(self) -> dict[int, PlayerDetail]:
        """
        Get all players in league.

        Args:
        ----
            data (dict[str, any]): league data.

        Returns:
        -------
            list[PlayerDetail]: Details of all players in the league.

        """
        return {player.id: player for player in self.bootstrap_data.elements}

    def get_player_summary(self, player_id: str) -> PlayerSummaryResponse:
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
        return PlayerSummaryResponse(**self.client.get(url).json)

    def get_player_by_id(
        self,
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
        player_summary = self.get_player_summary(player_id)

        return PlayerData(
            player_detail=bootstrap_data[player_id],
            fixtures=player_summary.fixtures,
            history=player_summary.history,
            history_past=player_summary.history_past,
        )
