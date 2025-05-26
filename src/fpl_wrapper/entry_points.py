"""Program entry points."""

import argparse
from pprint import pprint

import httpx

from fpl_wrapper.data_fetch.bootstrap_data import get_bootstrap_data
from fpl_wrapper.data_fetch.exception import (
    PhotoNotFoundError,
    ShirtNotFoundError,
)
from fpl_wrapper.data_fetch.fixtures import FixtureProvider
from fpl_wrapper.data_fetch.managers import Managers
from fpl_wrapper.data_fetch.players import Players
from fpl_wrapper.data_fetch.teams import Teams


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
    argparser.add_argument(
        "--gameweek", type=int, required=True, help="Gameweek number"
    )
    argparser.add_argument("--team_id", type=int, required=True, help="Team ID")
    args = argparser.parse_args()
    provider = FixtureProvider(httpx.Client())
    pprint(
        [
            fixture.model_dump_json()
            for fixture in provider.get_fixtures(
                httpx.Client(), args.gameweek, args.team_id
            )
        ]
    )


def get_league_data_entry() -> None:
    """Get league data."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-lid", "--league_id", type=str, required=True, help="League ID"
    )
    argparser.add_argument(
        "-p", "--page", type=int, required=True, help="Page number"
    )
    args = argparser.parse_args()
    provider = Managers(httpx.Client())
    pprint(
        provider.get_league_data(
            httpx.Client(), args.league_id, args.page
        ).model_dump(mode="json")
    )


def get_manager_gw_data_entry() -> None:
    """Get manager data for a specific gameweek."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-tid", "--team_id", type=str, required=True, help="Team ID"
    )
    argparser.add_argument(
        "-gw", "--gameweek", type=str, required=True, help="Gameweek"
    )
    args = argparser.parse_args()
    provider = Managers(httpx.Client())
    pprint(
        provider.get_manager_gw_data(
            httpx.Client(), args.team_id, args.gameweek
        ).model_dump(mode="json")
    )


def get_players_entry() -> None:
    """Get all players in league."""
    bootstrap = get_bootstrap_data(httpx.Client())
    pprint(Players(httpx.Client()).get_all_player_detail(bootstrap))


def get_teams_entry() -> None:
    """Get all teams in league."""
    pprint(Teams(httpx.Client()).get_teams())


def get_player_entry() -> None:
    """Get player by id."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "--player_id", type=int, required=True, help="Player ID"
    )
    args = argparser.parse_args()
    pprint(
        Players(httpx.Client())
        .get_player_by_id(args.player_id)
        .model_dump(mode="json")
    )


def get_player_photos_entry() -> None:
    """Get player photo."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "--player_id", type=int, required=True, help="Player ID"
    )
    args = argparser.parse_args()
    player = Players(httpx.Client()).get_player_detail(args.player_id)
    player.get_player_photo(output_directory="player_photos")


def get_player_photos_all_entry() -> None:
    """Get all player photos."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "--output_directory",
        type=str,
        default="player_photos",
        help="Output directory for player photos defaults to 'player_photos'",
        required=False,
    )
    args = argparser.parse_args()
    players = Players(httpx.Client()).get_all_player_detail()
    for player in players.values():
        try:
            player.get_player_photo(output_directory=args.output_directory)
        except PhotoNotFoundError as e:
            print(f"Error downloading photo for player {player.id}: {e}")  # noqa: T201
            continue


def get_team_crest_entry() -> None:
    """Get team crest."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--team_id", type=int, required=True, help="Team ID")
    args = argparser.parse_args()
    client = httpx.Client()
    team = Teams(client).get_team(args.team_id)
    team.get_team_crest(client)


def get_all_team_crests_entry() -> None:
    """Get all team crests."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "--output_directory", type=str, default="club_crests", required=False
    )
    args = argparser.parse_args()
    client = httpx.Client()
    teams = Teams(client).get_teams()
    for team in teams.values():
        try:
            team.get_team_crest(client, output_directory=args.output_directory)
        except PhotoNotFoundError as e:
            print(f"Error downloading crest for team {team.id}: {e}")  # noqa: T201
            continue


def get_team_shirt_entry() -> None:
    """Get team shirt."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--team_id", type=int, required=True)
    argparser.add_argument(
        "--output_directory",
        type=str,
        default="team_shirt",
        required=False,
        help="Output directory for team shirts",
    )
    argparser.add_argument(
        "--keeper-shirt",
        required=False,
        action="store_false",
    )
    args = argparser.parse_args()
    client = httpx.Client()
    team = Teams(client).get_team(args.team_id)

    try:
        if args.keeper_shirt:
            team.get_team_shirt(client, output_directory=args.output_directory)
        else:
            team.get_team_goalkeeper_shirt(client)
    except ShirtNotFoundError as e:
        print(f"Error downloading shirt for team {team.id}: {e}")  # noqa: T201


def get_all_team_shirts_entry() -> None:
    """Get all team shirts."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "--output_directory",
        type=str,
        default="team_shirts",
        required=False,
        help="Output directory for team shirts defaults to 'team_shirts'",
    )
    args = argparser.parse_args()
    client = httpx.Client()
    teams = Teams(client).get_teams()
    for team in teams.values():
        try:
            team.get_team_shirt(client, output_directory=args.output_directory)
            team.get_team_goalkeeper_shirt(
                client, output_directory=args.output_directory
            )
        except ShirtNotFoundError as e:
            print(f"Error downloading shirt for team {team.id}: {e}")  # noqa: T201
            continue
