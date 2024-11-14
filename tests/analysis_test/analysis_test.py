"""Test for the analysis functions. NOTE THESE ARE TESTS WHERE THE FUNCTION IS JUST CALLED THEY HAVE NOT BEEN FIXTURE TESTED YET."""

import httpx
from fpl.analysis.analysis import count_player_picks, get_most_common_formation, get_player_average_team, sort_player_by_count
from fpl.data_fetch.players import get_bootstrap_data
from fpl.input_parsing import parse_formation


def test_get_player_count(player_picks):
    """Test the count_player_picks function."""
    picks = count_player_picks(gw_picks=player_picks)
    assert picks[401] == 2

def test_sort_player_count(player_picks):
    """Run the analysis tests."""
    counts = count_player_picks(gw_picks=player_picks)
    sort_player_by_count(counts)


def test_get_player_average_formation():
    """Test the get_player_average_formation function."""
    formation = get_most_common_formation(player_id=3022638, gameweek_from=1, gameweek_to=10, bootstrap_data=get_bootstrap_data(httpx.Client()))
    assert formation.__str__() == "3-4-3-1"

def test_get_player_average_team():
    """Test the get_player_average_team function."""
    average_team = get_player_average_team(player_id=3022638, gameweek_from=1, gameweek_to=10, formation=parse_formation.parse_formation("3-4-3-1"), bootstrap_data=get_bootstrap_data(httpx.Client()))
