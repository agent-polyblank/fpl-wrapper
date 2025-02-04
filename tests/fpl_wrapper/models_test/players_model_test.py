"""Tests for models."""

from fpl_wrapper.model.players_models import (
    Fixture,
    History,
    HistoryPast,
    PlayerData,
    PlayerDetail,
)


def test_fixture_model(fixture_player_match_fixture_data):
    """Test fixture model."""
    fixture = Fixture(**fixture_player_match_fixture_data)
    assert fixture.id == 1
    assert fixture.team_h_score == 2
    assert fixture.team_a_score == 1


def test_history_model(fixture_history_data):
    """Test history model."""
    history = History(**fixture_history_data)
    assert history.total_points == 10
    assert history.goals_scored == 1


def test_history_past_model(fixture_history_past_data):
    """Test history past model."""
    history_past = HistoryPast(**fixture_history_past_data)
    assert history_past.season_name == "2022/23"
    assert history_past.total_points == 200


def test_player_data_model(fixture_player_data):
    """Test player data model."""
    player = PlayerData(**fixture_player_data)
    assert len(player.fixtures) == 1
    assert len(player.history) == 1
    assert len(player.history_past) == 1


def test_player_detail(fixture_player_detail_data):
    """Test player detail model."""
    player_detail = PlayerDetail(**fixture_player_detail_data)
    assert player_detail.first_name == "Fábio"
