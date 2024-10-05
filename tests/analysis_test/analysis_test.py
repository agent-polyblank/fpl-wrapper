"""Test for the analysis functions."""

from fpl.analysis.analysis import count_player_picks, sort_player_by_count


def test_get_player_count(player_picks):
    """Test the count_player_picks function."""
    picks = count_player_picks(gw_picks=player_picks)
    assert picks[401] == 2

def test_sort_player_count(player_picks):
    """Run the analysis tests."""
    counts = count_player_picks(gw_picks=player_picks)
    sort_player_by_count(counts)
