from pydantic_core import ValidationError
import pytest
from fpl_wrapper.model.managers_models import ChipsEnum, LeagueData, ManagerTeamData
from fpl_wrapper.model.players_models import Club


def test_league_data_model(fixture_league_data):
    """Test league data model."""
    league = LeagueData(**fixture_league_data)
    assert league.new_entries.has_next == False
    assert len(league.standings.results) == 50


def test_team_data(picks_data_no_chip):
    """Test TeamData model."""
    team_data = ManagerTeamData(**picks_data_no_chip)
    assert team_data is not None
    assert team_data.active_chip is None


def test_team_data_with_chip(fixture_picks_data_wildcard):
    """Test TeamData model."""
    team_data = ManagerTeamData(**fixture_picks_data_wildcard)
    assert team_data is not None
    assert team_data.active_chip == ChipsEnum.wildcard


def test_get_league_data_invalid_chip(fixture_picks_data_wildcard):
    """Test TeamData model. given an invalid chip."""
    picks = fixture_picks_data_wildcard
    picks["active_chip"] = "invalid_chip"
    with pytest.raises(ValidationError):
        team_data = ManagerTeamData(**picks)


def test_club(fixture_team_forest):
    """Test Club model."""
    club_data = Club(**fixture_team_forest)
    assert club_data is not None
