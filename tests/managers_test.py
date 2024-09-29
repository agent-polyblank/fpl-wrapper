
from unittest.mock import Mock
import httpx

from fpl.managers import get_league_data


def test_get_league_data(league_data):
    "Test get league data function."
    client = httpx.Client()

    mock_get_player_summary = Mock()
    mock_get_player_summary.return_value.json.return_value = league_data

    # Call the function with mocks
    result = get_league_data(client=client, league_id=1,page=1)

    assert result.league.name == "Arsenal"
