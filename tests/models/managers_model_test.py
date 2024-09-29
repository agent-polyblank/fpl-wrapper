from httpx import get
import httpx
from fpl.managers import get_manager_gw_data
from fpl.model.managers_models import LeagueData


def test_league_data_model(league_data):
    """Test league data model."""
    league = LeagueData(**league_data)
    assert league.new_entries.has_next == False
    assert len(league.standings.results) == 50


def test_get_manager_gw_data():
    """Test get picks."""
    pass
