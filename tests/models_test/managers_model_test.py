from uu import Error
from httpx import get
from pydantic_core import ValidationError
import pytest
from fpl.model.managers_models import ChipsEnum, LeagueData, TeamData


def test_league_data_model(league_data):
    """Test league data model."""
    league = LeagueData(**league_data)
    assert league.new_entries.has_next == False
    assert len(league.standings.results) == 50


def test_team_data(picks_data_no_chip):
    """Test TeamData model."""
    team_data = TeamData(**picks_data_no_chip)
    assert team_data is not None
    assert team_data.active_chip is None

def test_team_data_with_chip(picks_data_wildcard):
    """Test TeamData model."""
    team_data = TeamData(**picks_data_wildcard)
    assert team_data is not None
    assert team_data.active_chip == ChipsEnum.wildcard

def test_get_league_data_invalid_chip(picks_data_wildcard):
    """Test TeamData model. given an invalid chip."""
    picks = picks_data_wildcard
    picks["active_chip"] = "invalid_chip"
    with pytest.raises(ValidationError):
        team_data = TeamData(**picks)
