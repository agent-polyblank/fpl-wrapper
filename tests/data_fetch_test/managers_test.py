from unittest.mock import Mock
import httpx

from fpl.data_fetch.managers import get_league_data, get_manager_gw_data


def test_get_league_data(league_data):
    """Test get league data function."""
    client = httpx.Client()

    mock_get_player_summary = Mock()
    mock_get_player_summary.return_value.json.return_value = league_data

    # Call the function with mocks
    result = get_league_data(client=client, league_id=1, page=1)

    assert result.league.name == "Arsenal"


def test_get_manager_gw_data(picks_data_no_chip):
    """Test get_manager_gw_data function."""
    client = httpx.Client()

    mock_get_player_summary = Mock()
    mock_get_player_summary.return_value.json.return_value = picks_data_no_chip

    # Call the function with mocks
    result = get_manager_gw_data(client=client, team_id=1, gw=1)

    assert result is not None
    assert result.picks[0].element == 201
