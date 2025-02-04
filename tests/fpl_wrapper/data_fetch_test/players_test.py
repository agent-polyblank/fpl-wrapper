import httpx
import json
from unittest.mock import MagicMock, Mock

from fpl_wrapper.model.players_models import PlayerData
from fpl_wrapper.data_fetch.players import (
    get_bootstrap_data,
    get_player_by_id,
    get_players,
    get_teams,
)


def test_get_bootstrap_data(mocker, fixture_players_bootstrap_data):
    """Test the get_all_player_detail function with mocked dependencies."""

    client = mocker.Mock()
    response = mocker.Mock()
    response.json.return_value = fixture_players_bootstrap_data
    client.get.return_value = response
    result = get_bootstrap_data(client)

    assert len(result) == len(fixture_players_bootstrap_data["elements"])
    player = result["elements"][0]
    assert player["id"] == 1
    assert player["first_name"] == "Fábio"


def test_get_player_by_id(mocker,fixture_player_data, fixture_players_bootstrap_data):
    """Test the get_player_by_id function with mocked dependencies."""
    client = mocker.Mock()
    response = mocker.Mock()
    response.json.return_value = fixture_player_data
    client.get.return_value = response

    player_id = 1

    # Call the function with mocks
    result = get_player_by_id(
        client=client,
        player_id=player_id,
        bootstrap_data=get_players(fixture_players_bootstrap_data),
    )

    # Assert that the result is an instance of PlayerData
    assert isinstance(result, PlayerData)
    assert result.player_detail.web_name == "Fábio Vieira"


def test_get_players(fixture_players_bootstrap_data):
    """Test the get_players function."""
    players = get_players(fixture_players_bootstrap_data)
    assert len(players) == 1
    assert players[1].web_name == "Fábio Vieira"
    assert players[1].position == "Midfielder"


def test_get_clubs(fixture_team_bootstrap_data):
    """Test the get_teams function."""
    teams = get_teams(fixture_team_bootstrap_data)
    assert len(teams) == 2
    assert teams[0].name == "Nott'm Forest"
    assert teams[1].name == "Newcastle"
