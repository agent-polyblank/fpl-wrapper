"""Test for the analysis functions."""

from fpl.analysis.analysis import count_player_picks


def test_get_player_count(player_picks):
    """Test the count_player_picks function."""
    picks = count_player_picks(gw_picks=player_picks)
    assert picks[401] == 2 # Player with ID 401 was picked twice
