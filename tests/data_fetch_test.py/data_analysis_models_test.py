"""Tests for the data analysis models."""

from src.fpl.model.data_analysis import PlayerCount


def test_player_count():
    """Test player analysis."""
    player_count = PlayerCount(player_id=1, player_count=2)
    assert player_count["player_count"] == 2
    assert player_count["player_id"] == 1
