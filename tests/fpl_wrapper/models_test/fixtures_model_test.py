"""Tests for the fixtures model."""

from fpl_wrapper.model.players_models import Fixture


def test_match_data_model(fixture_player_event):
    """Test the fixtures model."""
    fixture = Fixture(**fixture_player_event)
    assert fixture.id == 1
    assert fixture.kickoff_time == "2024-08-16T19:00:00Z"
