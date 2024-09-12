from pydantic import ValidationError
import pytest
import httpx

from fpl.models import PlayerData, PlayerDetail
from fpl.shared import get_player_by_id

@pytest.fixture
def mock_player_data():
    return {
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
def test_get_player_by_id(mock_player_data, monkeypatch):
    class MockResponse:
        def json(self):
            return mock_player_data

    def mock_get(url):
        return MockResponse()

    monkeypatch.setattr(httpx, "get", mock_get)

    player_id = "1"
    player_data = get_player_by_id(player_id)
    
    assert isinstance(player_data, PlayerData)
    

