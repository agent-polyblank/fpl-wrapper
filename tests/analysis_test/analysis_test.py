"""Test for the analysis functions. NOTE THESE ARE TESTS WHERE THE FUNCTION IS JUST CALLED THEY HAVE NOT BEEN FIXTURE TESTED YET."""

import httpx
from fpl.analysis.analysis import (
    count_player_picks,
    get_most_common_formation,
)
from fpl.data_fetch.players import get_bootstrap_data, get_players


def test_count_player_picks(fixture_player_picks_list):
    """
    Test count player picks.
    """
    picks = count_player_picks(gw_picks=fixture_player_picks_list)
    assert (picks[201]) == 2


def test_get_most_common_formation(
    fixture_player_picks_list, fixture_player_detail_for_average_team
):
    get_most_common_formation(
        fixture_player_picks_list, fixture_player_detail_for_average_team
    )


def test_get_player_average_team(
    fixture_player_picks_list, fixture_player_detail_for_average_team
):
    # player_data = get_players(get_bootstrap_data(httpx.Client()))
    # data = {}
    # for fixture in fixture_player_picks_list:
    #     for player in fixture.picks:
    #         data[player.element] = player_data[player.element]
    # assert data is not {}
    pass

def test_get_player_picks():
    pass


def sort_player_by_count():
    pass


def test_sort_player_count():
    pass
