"""Program entry points."""

import argparse
import json
from pathlib import Path
from pprint import pprint

import httpx
from loguru import logger

from fpl_wrapper.data_fetch.bootstrap_data import get_bootstrap_data
from fpl_wrapper.data_fetch.exception import (
    PhotoNotFoundError,
    ShirtNotFoundError,
)
from fpl_wrapper.data_fetch.fixtures import FixtureProvider
from fpl_wrapper.data_fetch.managers import Managers
from fpl_wrapper.data_fetch.players import Players
from fpl_wrapper.data_fetch.teams import Teams


def get_bootstrap_data_entry() -> None:
    """Get bootstrap data."""
    argparser = argparse.ArgumentParser("Bootstrap Data")
    argparser.add_argument(
        "--output_file", type=str, required=False, help="Output file path"
    )
    args = argparser.parse_args()
    client = httpx.Client()
    data = get_bootstrap_data(client)
    if args.output_file:
        path = Path(args.output_file)
    else:
        path = Path("results/bootstrap_data.json")
    if not path.parent.exists():
        path.parent.mkdir(parents=True)
    with path.open("w") as f:
        f.write(data.model_dump_json(indent=2))


def get_all_player_data_entry() -> None:
    """Get all player data."""
    argparser = argparse.ArgumentParser("All Player Data")
    argparser.add_argument(
        "--output_file",
        type=str,
        required=False,
        help="Output file path",
        default="results/all_player_data.json",
    )
    args = argparser.parse_args()
    client = httpx.Client()
    players = Players(client).get_all_player_detail()
    path = Path(args.output_file)
    if not path.parent.exists():
        path.parent.mkdir(parents=True)
    with path.open("w") as f:
        f.write(json.dumps(players, indent=2))


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
    argparser.add_argument(
        "--output_file",
        type=str,
        required=False,
        help="Output file path",
        default="results/fixtures.json",
    )
    args = argparser.parse_args()
    provider = FixtureProvider(httpx.Client())
    fixtures = provider.get_fixtures(args.gameweek, args.team_id)
    path = Path(args.output_file)
    if not path.parent.exists():
        path.parent.mkdir(parents=True)
    with path.open("w") as f:
        f.write(
            json.dumps(fixtures, indent=2, default=lambda x: x.model_dump())
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
    argparser.add_argument(
        "-o", "--output_file", type=str, required=False, help="Output file path"
    )
    args = argparser.parse_args()
    provider = Managers(httpx.Client())
    logger.info(
        f"Fetching league data for {args.league_id} on page {args.page}"
    )
    if args.output_file:
        path = Path(args.output_file)
    else:
        path = Path(f"results/league_data_{args.league_id}_{args.page}.json")
    with path.open("w") as f:
        f.write(
            provider.get_league_data(args.league_id, args.page).model_dump_json(
                indent=2
            )
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
    argparser.add_argument("--output_file", type=str, required=True)

    args = argparser.parse_args()
    provider = Managers(httpx.Client())

    if args.output_file:
        path = Path(args.output_file)
    else:
        path = Path(
            f"results/manager_gw_data_{args.team_id}_{args.gameweek}.json"
        )
    if not path.parent.exists():
        path.parent.mkdir(parents=True)
    with path.open("w") as f:
        f.write(
            provider.get_manager_gw_data(
                args.team_id, args.gameweek
            ).model_dump_json(indent=2)
        )


def get_manager_all_gw_data_entry() -> None:
    """Get manager data for all gameweeks."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-tid", "--team_id", type=str, required=True, help="Team ID"
    )
    argparser.add_argument("--output_file", type=str, required=True)

    args = argparser.parse_args()
    provider = Managers(httpx.Client())

    if args.output_file:
        path = Path(args.output_file)
    else:
        path = Path(f"results/manager_all_gw_data_{args.team_id}.json")

    if not path.parent.exists():
        path.parent.mkdir(parents=True)
    with path.open("w") as f:
        import json

        logger.info(f"Fetching all gameweek data for team {args.team_id}")
        data = provider.get_manager_all_gw_data(args.team_id)
        f.write(
            json.dumps(
                [item.model_dump(mode="json") for item in data], indent=2
            )
        )


def get_league_standings_entry() -> None:
    """Get league standings."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-lid", "--league_id", type=str, required=True, help="League ID"
    )
    argparser.add_argument(
        "-p", "--page", type=int, required=True, help="Page number"
    )
    argparser.add_argument(
        "--output_file", type=str, required=False, help="Output file path"
    )
    args = argparser.parse_args()
    provider = Managers(httpx.Client())
    standings = provider.get_league_data(args.league_id, args.page).standings
    if args.output_file:
        path = Path(args.output_file)
    else:
        path = Path(
            f"results/league_standings_{args.league_id}_{args.page}.json"
        )
    if not path.parent.exists():
        path.parent.mkdir(parents=True)
    with path.open("w") as f:
        f.write(standings.model_dump_json(indent=2))


def get_gameweek_data_for_each_manager_for_each_gameweek_entry() -> None:
    """Get gameweek data for each manager for each gameweek."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-lid", "--league_id", type=str, required=True, help="League ID"
    )
    argparser.add_argument(
        "-p", "--page", type=int, required=True, help="Page number"
    )
    argparser.add_argument(
        "-o",
        "--output_file",
        type=str,
        required=True,
        help="Output file path",
        default="/results/gameweek_data.json",
    )
    args = argparser.parse_args()
    provider = Managers(httpx.Client())
    league_data = provider.get_league_data(args.league_id, args.page)
    path = Path(args.output_file)
    if not path.parent.exists():
        path.parent.mkdir(parents=True)
    with path.open("w") as f:
        result = {}
        for manager in league_data.standings.results:
            data = provider.get_manager_all_gw_data(str(manager.entry))
            result[str(manager.entry)] = [
                item.model_dump(mode="json") for item in data
            ]
        json.dump(result, f, indent=2)


def get_players_entry() -> None:
    """Get all players in league."""
    pprint(Players(httpx.Client()).get_all_player_detail())


def get_teams_entry() -> None:
    """Get all teams in league."""
    argparser = argparse.ArgumentParser("Get Teams")
    argparser.add_argument(
        "--output_file",
        type=str,
        required=False,
        help="Output file path",
        default="results/teams.json",
    )
    args = argparser.parse_args()
    path = Path(args.output_file)
    if not path.parent.exists():
        path.parent.mkdir(parents=True)
    client = httpx.Client()
    with path.open("w") as f:
        json.dump(
            Teams(client).get_teams(),
            f,
            indent=2,
            default=lambda x: x.model_dump(mode="json"),
        )


def get_all_player_detail_entry() -> None:
    """Get all player details."""
    argparser = argparse.ArgumentParser("Get All Player Details")
    argparser.add_argument(
        "--output_file",
        type=str,
        required=False,
        help="Output file path",
        default="results/all_player_detail.json",
    )
    args = argparser.parse_args()
    path = Path(args.output_file)
    client = httpx.Client()
    players_class = Players(client)
    players = players_class.get_all_player_detail()
    with path.open("w", encoding="utf8") as f:
        json.dump(
            {
                str(key): players_class.get_player_by_id(key).model_dump(
                    mode="json"
                )
                for key in players
            },
            f,
            indent=2,
            ensure_ascii=False,
        )


def get_player_entry() -> None:
    """Get player by id."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "--player_id", type=int, required=True, help="Player ID"
    )
    argparser.add_argument(
        "--output_file", type=str, required=False, help="Output file path"
    )
    args = argparser.parse_args()
    if args.output_file:
        path = Path(args.output_file)
    else:
        path = Path(f"results/player_{args.player_id}.json")
    if not path.parent.exists():
        path.parent.mkdir(parents=True)
    with path.open("w", encoding="utf8") as f:
        f.write(
            Players(httpx.Client())
            .get_player_by_id(args.player_id)
            .model_dump_json(indent=2)
        )


def get_player_photos_entry() -> None:
    """Get player photo."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "--player_id", type=int, required=True, help="Player ID"
    )
    args = argparser.parse_args()
    player = Players(httpx.Client()).get_player_detail(args.player_id)
    logger.info(f"Downloading photo for player {player.id}")
    player.get_player_photo(output_directory="results/player_photos")


def get_player_photos_all_entry() -> None:
    """Get all player photos."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "--output_directory",
        type=str,
        default="results/player_photos",
        help="Output directory for player photos defaults to 'player_photos'",
        required=False,
    )
    args = argparser.parse_args()
    players = Players(httpx.Client()).get_all_player_detail()
    for player in players.values():
        try:
            player.get_player_photo(output_directory=args.output_directory)
        except PhotoNotFoundError as e:
            logger.error(f"Photo for player {player.web_name} not found")
            logger.error(f"They may not have a photo yet: {e}")
            continue


def get_team_crest_entry() -> None:
    """Get team crest."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--team_id", type=int, required=True, help="Team ID")
    args = argparser.parse_args()
    client = httpx.Client()
    team = Teams(client).get_team(args.team_id)
    logger.info(f"Downloading crest for team {team.id}")
    team.get_team_crest(client=client, output_directory="results/club_crests")


def get_all_team_crests_entry() -> None:
    """Get all team crests."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "--output_directory",
        type=str,
        default="results/club_crests",
        required=False,
    )
    args = argparser.parse_args()
    client = httpx.Client()
    teams = Teams(client).get_teams()
    for team in teams.values():
        try:
            logger.info(f"Downloading crest for team {team.id}")
            team.get_team_crest(client, output_directory=args.output_directory)
        except PhotoNotFoundError as e:
            logger.error(f"Error downloading crest for team {team.id}: {e}")
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
            logger.info(f"Downloading shirt for team {team.id}")
            team.get_team_shirt(client, output_directory=args.output_directory)
        else:
            logger.info(f"Downloading goalkeeper shirt for team {team.id}")
            team.get_team_goalkeeper_shirt(client)
    except ShirtNotFoundError as e:
        logger.error(f"Error downloading shirt for team {team.id}: {e}")


def get_all_team_shirts_entry() -> None:
    """Get all team shirts."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "--output_directory",
        type=str,
        default="results/team_shirts",
        required=False,
        help="Output directory for team shirts defaults to 'team_shirts'",
    )
    args = argparser.parse_args()
    client = httpx.Client()
    teams = Teams(client).get_teams()
    for team in teams.values():
        try:
            logger.info(f"Downloading shirt for team {team.id}")
            team.get_team_shirt(client, output_directory=args.output_directory)
            logger.info(f"Downloading goalkeeper shirt for team {team.id}")
            team.get_team_goalkeeper_shirt(
                client, output_directory=args.output_directory
            )
        except ShirtNotFoundError as e:
            logger.error(f"Error downloading shirt for team {team.id}: {e}")
            continue


def get_manager_data_entry() -> None:
    """Get manager data."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-mid", "--manager_id", type=str, required=True, help="Manager ID"
    )
    argparser.add_argument(
        "-o", "--output_file", type=str, required=False, help="Output file path"
    )
    args = argparser.parse_args()
    provider = Managers(httpx.Client())
    manager_data = provider.get_all_manager_data(args.manager_id)
    if args.output_file:
        path = Path(args.output_file)
    else:
        path = Path(f"manager_data_{args.manager_id}.json")
    with path.open("w", encoding="utf8") as f:
        f.write(manager_data.model_dump_json(indent=2))


def get_manager_full_data_from_league_entry() -> None:
    """Get manager data from league entry."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-lid", "--league_id", type=str, required=True, help="League ID"
    )
    argparser.add_argument(
        "-o", "--output_file", type=str, required=False, help="Output file path"
    )
    argparser.add_argument(
        "-p", "--page", type=int, required=True, help="Page number"
    )
    args = argparser.parse_args()
    provider = Managers(httpx.Client())
    league_data = provider.get_league_data(args.league_id, args.page)
    if args.output_file:
        path = Path(args.output_file)
    else:
        path = Path(
            f"manager_data_from_league_{args.league_id}_{args.page}.json"
        )
    with path.open("w", encoding="utf8") as f:
        result = {}
        for manager in league_data.standings.results:
            logger.info(f"Fetching data for manager {manager.entry}")
            data = provider.get_all_manager_data(str(manager.entry))
            result[str(manager.entry)] = data.model_dump(mode="json")
        json.dump(result, f, indent=2, ensure_ascii=False)


def get_all_managers_in_league_entry() -> None:
    """Get all managers in league."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-lid", "--league_id", type=str, required=True, help="League ID"
    )
    argparser.add_argument(
        "-o", "--output_file", type=str, required=False, help="Output file path"
    )
    args = argparser.parse_args()
    provider = Managers(httpx.Client())
    league_data = provider.get_league_data(args.league_id, 1)
    if args.output_file:
        path = Path(args.output_file)
    else:
        path = Path(f"all_managers_in_league_{args.league_id}.json")
    with path.open("w", encoding="utf8") as f:
        result = {}
        for manager in league_data.standings.results:
            data = provider.get_manager_basic_info(str(manager.entry))
            result[str(manager.entry)] = data.model_dump(mode="json")
        json.dump(result, f, indent=2, ensure_ascii=False)


def get_full_manager_data_for_league_entry() -> None:
    """Get full manager data for league."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-lid", "--league_id", type=str, required=True, help="League ID"
    )
    argparser.add_argument(
        "-o", "--output_file", type=str, required=False, help="Output file path"
    )
    args = argparser.parse_args()
    provider = Managers(httpx.Client())
    league_data = provider.get_league_data(args.league_id, 1)
    if args.output_file:
        path = Path(args.output_file)
    else:
        path = Path(f"manager_data_{args.league_id}.json")

    with path.open("w", encoding="utf8") as f:
        result = {}
        for manager in league_data.standings.results:
            logger.info(f"Fetching data for manager {manager.entry}")
            data = provider.get_all_manager_data(str(manager.entry))
            result[str(manager.entry)] = data.model_dump(mode="json")
        json.dump(result, f, indent=2, ensure_ascii=False)


def get_full_manager_data_for_league_max_pages_entry() -> None:
    """Get full manager data for league across all pages."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-lid", "--league_id", type=str, required=True, help="League ID"
    )
    argparser.add_argument(
        "-o", "--output_file", type=str, required=False, help="Output file path"
    )
    argparser.add_argument("-mp", "--max-pages", type=int, default=1000)
    args = argparser.parse_args()
    provider = Managers(httpx.Client())

    if args.output_file:
        path = Path(args.output_file)
    else:
        path = Path(
            f"manager_data_{args.league_id}_pages_{args.max_pages}.json"
        )
    with path.open("w", encoding="utf8") as f:
        result = {}
        for page in range(1, args.max_pages + 1):
            logger.info(f"Fetching page {page} for league {args.league_id}")
            league_data_page = provider.get_league_data(args.league_id, page)
            for manager in league_data_page.standings.results:
                logger.info(f"Fetching data for manager {manager.entry}")
                data = provider.get_all_manager_data(str(manager.entry))
                result[str(manager.entry)] = data.model_dump(mode="json")
        json.dump(result, f, indent=2, ensure_ascii=False)
