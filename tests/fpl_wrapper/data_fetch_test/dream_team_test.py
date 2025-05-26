
import httpx
from fpl_wrapper.data_fetch.dream_team import DreamTeamFetcher
from fpl_wrapper.model.dream_team import DreamTeam


def test_get_dream_team(mocker,fixture_dream_team) -> None:
    """
    Test the get_dream_team method of the FPLWrapper class.
    """
    client = mocker.Mock()
    response = mocker.Mock()
    response.json.return_value = fixture_dream_team
    client.get.return_value = response
    dream_team = DreamTeamFetcher(client=client)
    dream_team = dream_team.get_dream_team()
    assert isinstance(dream_team, DreamTeam)
