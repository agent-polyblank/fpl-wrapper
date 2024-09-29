import httpx
import json
from unittest.mock import MagicMock, Mock
from pydantic import ValidationError

from fpl.model.players_models import PlayerData
from fpl.data_fetch.players import get_all_player_detail, get_player_by_id


def test_get_all_player_detail(mocker, bootstrap_data):
    # Mock the httpx.Client.get method to return this mock response
    mocker.patch(
        "httpx.Client.get",
        return_value=MagicMock(text=json.dumps(bootstrap_data)),
    )

    # Create a client instance
    client = httpx.Client()

    # Call the function
    result = get_all_player_detail(client)

    # Verify the result is a list with one PlayerDetail object
    assert len(result) == len(
        bootstrap_data["elements"]
    )  # Match length of data
    player = result[0]
    assert player.id == 1
    assert player.first_name == "Fábio"


def test_get_player_by_id(player_data, bootstrap_data):
    """Test the get_player_by_id function with mocked dependencies."""

    client = httpx.Client()

    mock_get_player_summary = Mock()
    mock_get_player_summary.return_value.json.return_value = player_data

    mock_get_all_player_detail = Mock()
    mock_get_all_player_detail.return_value = bootstrap_data["elements"]

    player_id = 1

    # Call the function with mocks
    result = get_player_by_id(
        client=client,
        player_id=player_id,
        get_player_summary_func=mock_get_player_summary,
        get_all_player_detail_func=mock_get_all_player_detail,
    )

    # Assert that the result is an instance of PlayerData
    assert isinstance(result, PlayerData)
    assert result.player_detail.web_name == "Fábio Vieira"
