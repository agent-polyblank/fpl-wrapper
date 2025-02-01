"""Program entry points."""

import argparse
import pprint

import httpx

from fpl.data_fetch.fixtures import get_fixtures
from fpl.data_fetch.managers import get_league_data, get_manager_gw_data
from fpl.data_fetch.players import (
    get_bootstrap_data,
    get_player_summary,
    get_players,
)


def get_fixtures_entry() -> None:
    """
    Get fixtures.

    Args:
    ----
        client (httpx.Client): HTTP client instance.

    Returns:
    -------
        list[dict]: List of fixtures.

    """
    pprint.pprint(get_fixtures(httpx.Client()))


def get_league_data_entry() -> None:
    """
    Get league data and standings. This data is paginated.

    Args:
    ----
        client (httpx.Client): HTTP client instance.
        league_id (str): League id.
        page (int): Page number.

    Returns:
    -------
        dict: League data.

    """
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--league_id", type=str)
    argparser.add_argument("--page", type=int)
    args = argparser.parse_args()
    pprint.pprint(get_league_data(httpx.Client(), args.league_id, args.page))


def get_manager_gw_data_entry() -> None:
    """Get manager data for a specific gameweek."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--team_id", type=str)
    argparser.add_argument("--gw", type=str)
    args = argparser.parse_args()
    pprint.pprint(get_manager_gw_data(httpx.Client(), args.team_id, args.gw))


def get_players_entry() -> None:
    """Get all players in league."""
    bootstrap = get_bootstrap_data(httpx.Client())
    pprint.pprint(get_players(bootstrap))


def get_player() -> None:
    """Get player by id."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--player_id", type=str)
    args = argparser.parse_args()
    pprint.pprint(get_player_summary(httpx.Client(), args.player_id))
