"""Tests for the fixtures model."""

from fpl.model.fixture_models import MatchData


def test_match_data_model(fixture_match_fixture):
    """Test the fixtures model."""
    fixture = MatchData(**fixture_match_fixture)
    assert fixture.id == 1
    assert fixture.kickoff_time == "2024-08-16T19:00:00Z"
