from httpx import get
from fpl.model.managers_models import LeagueData, TeamData


def test_league_data_model(league_data):
    """Test league data model."""
    league = LeagueData(**league_data)
    assert league.new_entries.has_next == False
    assert len(league.standings.results) == 50


def test_team_data(picks_data):
    """Test TeamData model."""
    team_data = TeamData(**picks_data)
    assert team_data is not None
