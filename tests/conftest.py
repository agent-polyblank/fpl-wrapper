"""Fixtures for tests."""

import pytest


@pytest.fixture
def fixture_data():
    """Fixture for player fixture data."""
    return {
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

@pytest.fixture
def history_data():
    """Fixture for current season data"""
    return {
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

@pytest.fixture
def history_past_data():
    """Fixture for past season data data."""
    return {
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


@pytest.fixture
def player_detail_data():
    """Fixture for player detail data."""
    return {
        "chance_of_playing_next_round": 0,
        "chance_of_playing_this_round": 0,
        "code": 438098,
        "cost_change_event": 0,
        "cost_change_event_fall": 0,
        "cost_change_start": -1,
        "cost_change_start_fall": 1,
        "dreamteam_count": 0,
        "element_type": 3,
        "ep_next": "0.0",
        "ep_this": "0.0",
        "event_points": 0,
        "first_name": "Fábio",
        "form": "0.0",
        "id": 1,
        "in_dreamteam": False,
        "news": "Has joined Portuguese side FC Porto on loan for the 2024/25 season",
        "news_added": "2024-08-29T11:06:25.241953Z",
        "now_cost": 54,
        "photo": "438098.jpg",
        "points_per_game": "0.0",
        "second_name": "Ferreira Vieira",
        "selected_by_percent": "0.0",
        "special": False,
        "squad_number": None,
        "status": "u",
        "team": 1,
        "team_code": 3,
        "total_points": 0,
        "transfers_in": 439,
        "transfers_in_event": 0,
        "transfers_out": 2172,
        "transfers_out_event": 664,
        "value_form": "0.0",
        "value_season": "0.0",
        "web_name": "Fábio Vieira",
        "region": None,
        "minutes": 0,
        "goals_scored": 0,
        "assists": 0,
        "clean_sheets": 0,
        "goals_conceded": 0,
        "own_goals": 0,
        "penalties_saved": 0,
        "penalties_missed": 0,
        "yellow_cards": 0,
        "red_cards": 0,
        "saves": 0,
        "bonus": 0,
        "bps": 0,
        "influence": "0.0",
        "creativity": "0.0",
        "threat": "0.0",
        "ict_index": "0.0",
        "starts": 0,
        "expected_goals": "0.00",
        "expected_assists": "0.00",
        "expected_goal_involvements": "0.00",
        "expected_goals_conceded": "0.00",
        "influence_rank": 628,
        "influence_rank_type": 284,
        "creativity_rank": 627,
        "creativity_rank_type": 286,
        "threat_rank": 617,
        "threat_rank_type": 280,
        "ict_index_rank": 631,
        "ict_index_rank_type": 287,
        "corners_and_indirect_freekicks_order": None,
        "corners_and_indirect_freekicks_text": "",
        "direct_freekicks_order": None,
        "direct_freekicks_text": "",
        "penalties_order": None,
        "penalties_text": "",
        "expected_goals_per_90": 0,
        "saves_per_90": 0,
        "expected_assists_per_90": 0,
        "expected_goal_involvements_per_90": 0,
        "expected_goals_conceded_per_90": 0,
        "goals_conceded_per_90": 0,
        "now_cost_rank": 167,
        "now_cost_rank_type": 104,
        "form_rank": 627,
        "form_rank_type": 286,
        "points_per_game_rank": 627,
        "points_per_game_rank_type": 286,
        "selected_rank": 593,
        "selected_rank_type": 260,
        "starts_per_90": 0,
        "clean_sheets_per_90": 0
    }


@pytest.fixture
def player_data(fixture_data, history_data, history_past_data):
    return {
        "fixtures": [fixture_data],
        "history": [history_data],
        "history_past": [history_past_data]
    }

@pytest.fixture
def bootstrap_data(player_detail_data):
    """Fixture for bootstrap data."""
    return {
        "elements": [player_detail_data]
    }

@pytest.fixture
def league_data():
    """Fixture for league data."""
    return {
    "new_entries": {
        "has_next": False,
        "page": 1,
        "results": []
    },
    "last_updated_data": "2024-09-28T18:28:41Z",
    "league": {
        "id": 507369,
        "name": "Fish and chips",
        "created": "2024-07-29T09:57:35.177916Z",
        "closed": False,
        "max_entries": None,
        "league_type": "x",
        "scoring": "c",
        "admin_entry": 1581117,
        "start_event": 1,
        "code_privacy": "p",
        "has_cup": True,
        "cup_league": None,
        "rank": None
    },
    "standings": {
        "has_next": False,
        "page": 1,
        "results": [
            {
                "id": 17368194,
                "event_total": 12,
                "player_name": "Teagan Erasmus",
                "rank": 1,
                "last_rank": 1,
                "rank_sort": 1,
                "total": 334,
                "entry": 1581117,
                "entry_name": "Upamaguire"
            },
            {
                "id": 36468493,
                "event_total": 16,
                "player_name": "Tyler Moss",
                "rank": 2,
                "last_rank": 2,
                "rank_sort": 2,
                "total": 262,
                "entry": 743451,
                "entry_name": "CPT!CITYZENS"
            }
        ]
    }
}
