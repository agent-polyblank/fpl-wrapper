"""Dream team."""

import httpx

from fpl_wrapper.data_fetch.players import Players
from fpl_wrapper.model.dream_team import DreamTeam
from fpl_wrapper.model.players_models import PlayerDetail


class DreamTeamFetcher:
    """Class to fetch the dream team from the FPL API."""

    def __init__(self, client: httpx.Client) -> None:
        """
        Initialize the DreamTeamFetcher with an HTTP client.

        Args:
        ----
            client (httpx.Client): HTTP client instance.
                Defaults to a new instance.

        """
        self.client = client

    def get_dream_team(self) -> DreamTeam:
        """
        Get the dream team from the FPL API.

        Returns
        -------
            dict: Dream team data.

        """
        response = self.client.get(
            "https://fantasy.premierleague.com/api/dream-team/"
        )
        return DreamTeam.model_validate(response.json())

    def get_dream_team_with_player_details(self) -> list[PlayerDetail]:
        """
        Get the dream team with player details.

        Returns
        -------
            DreamTeam: Dream team model with player details.

        """
        dream_team = self.get_dream_team()
        player_detail_getter = Players(client=self.client)
        return [
            player_detail_getter.get_player_detail(player.element)
            for player in dream_team.team
        ]
