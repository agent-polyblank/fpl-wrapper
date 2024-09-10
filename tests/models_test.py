"""Tests for the models module."""

import pytest
from pydantic import ValidationError
from src.fpl.models import Fixture, History, HistoryPast, PlayerData

def test_fixture_model():
    """Test fixture model."""
    fixture_data = {
        "id": 1,
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
    fixture = Fixture(**fixture_data)
    assert fixture.id == 1
    assert fixture.team_h_score == 2

def test_history_model():
    """Test history model."""
    history_data = {
        "element": 1,
        "fixture": 1,
        "opponent_team": 2,
        "total_points": 10,
        "was_home": True,
        "kickoff_time": "2023-10-01T12:30:00Z",
        "team_h_score": 2,
        "team_a_score": 1,
        "round": 1,
        "minutes": 90,
        "goals_scored": 1,
        "assists": 1,
        "clean_sheets": 1,
        "goals_conceded": 0,
        "own_goals": 0,
        "penalties_saved": 0,
        "penalties_missed": 0,
        "yellow_cards": 0,
        "red_cards": 0,
        "saves": 0,
        "bonus": 3,
        "bps": 30,
        "influence": "100.0",
        "creativity": "50.0",
        "threat": "75.0",
        "ict_index": "225.0",
        "starts": 1,
        "expected_goals": "0.5",
        "expected_assists": "0.3",
        "expected_goal_involvements": "0.8",
        "expected_goals_conceded": "0.2",
        "value": 100,
        "transfers_balance": 10,
        "selected": 1000,
        "transfers_in": 50,
        "transfers_out": 40
    }
    history = History(**history_data)
    assert history.total_points == 10
    assert history.goals_scored == 1

def test_history_past_model():
    """Test history past model."""
    history_past_data = {
        "season_name": "2022/23",
        "element_code": 1,
        "start_cost": 100,
        "end_cost": 110,
        "total_points": 200,
        "minutes": 3000,
        "goals_scored": 20,
        "assists": 10,
        "clean_sheets": 15,
        "goals_conceded": 25,
        "own_goals": 0,
        "penalties_saved": 0,
        "penalties_missed": 1,
        "yellow_cards": 3,
        "red_cards": 0,
        "saves": 0,
        "bonus": 30,
        "bps": 300,
        "influence": "500.0",
        "creativity": "200.0",
        "threat": "300.0",
        "ict_index": "1000.0",
        "starts": 35,
        "expected_goals": "10.0",
        "expected_assists": "5.0",
        "expected_goal_involvements": "15.0",
        "expected_goals_conceded": "20.0"
    }
    history_past = HistoryPast(**history_past_data)
    assert history_past.season_name == "2022/23"
    assert history_past.total_points == 200

def test_player_data_model():
    """Test player data model."""
    player_data = {
        "fixtures": [
            {
                "id": 1,
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
        ],
        "history": [
            {
                "element": 1,
                "fixture": 1,
                "opponent_team": 2,
                "total_points": 10,
                "was_home": True,
                "kickoff_time": "2023-10-01T12:30:00Z",
                "team_h_score": 2,
                "team_a_score": 1,
                "round": 1,
                "minutes": 90,
                "goals_scored": 1,
                "assists": 1,
                "clean_sheets": 1,
                "goals_conceded": 0,
                "own_goals": 0,
                "penalties_saved": 0,
                "penalties_missed": 0,
                "yellow_cards": 0,
                "red_cards": 0,
                "saves": 0,
                "bonus": 3,
                "bps": 30,
                "influence": "100.0",
                "creativity": "50.0",
                "threat": "75.0",
                "ict_index": "225.0",
                "starts": 1,
                "expected_goals": "0.5",
                "expected_assists": "0.3",
                "expected_goal_involvements": "0.8",
                "expected_goals_conceded": "0.2",
                "value": 100,
                "transfers_balance": 10,
                "selected": 1000,
                "transfers_in": 50,
                "transfers_out": 40
            }
        ],
        "history_past": [
            {
                "season_name": "2022/23",
                "element_code": 1,
                "start_cost": 100,
                "end_cost": 110,
                "total_points": 200,
                "minutes": 3000,
                "goals_scored": 20,
                "assists": 10,
                "clean_sheets": 15,
                "goals_conceded": 25,
                "own_goals": 0,
                "penalties_saved": 0,
                "penalties_missed": 1,
                "yellow_cards": 3,
                "red_cards": 0,
                "saves": 0,
                "bonus": 30,
                "bps": 300,
                "influence": "500.0",
                "creativity": "200.0",
                "threat": "300.0",
                "ict_index": "1000.0",
                "starts": 35,
                "expected_goals": "10.0",
                "expected_assists": "5.0",
                "expected_goal_involvements": "15.0",
                "expected_goals_conceded": "20.0"
            }
        ]
    }
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
