import pytest
from pydantic import ValidationError
from fpl.models import Fixture, History, HistoryPast, PlayerData, PlayerDetail
from tests.conftest import player_detail_data

def test_fixture_model(fixture_data):
    """Test fixture model."""
    fixture = Fixture(**fixture_data)
    assert fixture.id == 1
    assert fixture.team_h_score == 2
    assert fixture.team_a_score == 1

def test_history_model(history_data):
    """Test history model."""
    history = History(**history_data)
    assert history.total_points == 10
    assert history.goals_scored == 1

def test_history_past_model(history_past_data):
    """Test history past model."""
    history_past = HistoryPast(**history_past_data)
    assert history_past.season_name == "2022/23"
    assert history_past.total_points == 200

def test_player_data_model(player_data):
    """Test player data model."""
    player = PlayerData(**player_data)
    assert len(player.fixtures) == 1
    assert len(player.history) == 1
    assert len(player.history_past) == 1

def test_invalid_fixture_model():
    """Test invalid fixture model."""
    invalid_fixture_data = {
        "id": "invalid_id",  # id should be an int
        "code": 100,
        "team_h": 1,
        "team_h_score": 2,
        "team_a": 2,
        "team_a_score": 1,
        "event": 1,
        "finished": True,
        "minutes": 90,
        "provisional_start_time": False,
        "kickoff_time": "2023-10-01T12:30:00Z",
        "event_name": "Gameweek 1",
        "is_home": True,
        "difficulty": 3
    }
    with pytest.raises(ValidationError):
        Fixture(**invalid_fixture_data)

def test_player_detail(player_detail_data):
    """Test player detail model."""
    player_detail = PlayerDetail(**player_detail_data)
    assert player_detail.first_name == "Fábio"