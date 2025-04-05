"""Program entry points."""

import argparse
from pprint import pprint

import httpx

from fpl_wrapper.data_fetch.bootstrap_data import get_bootstrap_data
from fpl_wrapper.data_fetch.fixtures import get_fixtures
from fpl_wrapper.data_fetch.managers import get_league_data, get_manager_gw_data
from fpl_wrapper.data_fetch.players import (
    get_player_summary,
    get_players,
)
from fpl_wrapper.data_fetch.teams import get_teams


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
    argparser = argparse.ArgumentParser("Fixtures")
    argparser.add_argument("--gameweek", type=int)
    argparser.add_argument("--team_id", type=int)
    args = argparser.parse_args()
    pprint(
        [
            fixture.model_dump_json()
            for fixture in get_fixtures(
                httpx.Client(), args.gameweek, args.team_id
            )
        ]
    )


def get_league_data_entry() -> None:
    """Get league data."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-lid", "--league_id", type=str, required=True)
    argparser.add_argument("-p", "--page", type=int, required=True)
    args = argparser.parse_args()
    pprint(
        get_league_data(httpx.Client(), args.league_id, args.page).model_dump(
            mode="json"
        )
    )


def get_manager_gw_data_entry() -> None:
    """Get manager data for a specific gameweek."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-tid", "--team_id", type=str, required=True)
    argparser.add_argument("-gw", "--gameweek", type=str, required=True)
    args = argparser.parse_args()
    pprint(
        get_manager_gw_data(
            httpx.Client(), args.team_id, args.gameweek
        ).model_dump(mode="json")
    )


def get_players_entry() -> None:
    """Get all players in league."""
    bootstrap = get_bootstrap_data(httpx.Client())
    pprint(get_players(bootstrap).model_dump(mode="json"))


def get_teams_entry() -> None:
    """Get all teams in league."""
    get_teams(get_bootstrap_data(httpx.Client()))


def get_player() -> None:
    """Get player by id."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--player_id", type=str)
    args = argparser.parse_args()
    pprint(get_player_summary(httpx.Client(), args.player_id))
