from fpl_wrapper.data_fetch.bootstrap_data import get_bootstrap_data
from fpl_wrapper.data_fetch.teams import get_teams
from fpl_wrapper.model.players_models import PlayerData
from fpl_wrapper.data_fetch.players import (
    get_player_by_id,
    get_players,
)


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
