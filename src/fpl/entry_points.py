"""Entry point for module fpl."""

import logging
from argparse import ArgumentParser

import httpx

from fpl.analysis.analysis import (
    get_most_common_formation,
    get_player_average_team,
    get_player_picks,
)
from fpl.data_fetch.players import get_bootstrap_data, get_players
from fpl.input_parsing.parse_formation import parse_formation
from fpl.model.data_analysis import GameweekRange


def main() -> None:
    """FPL entry."""
    parser = ArgumentParser("fpl")
    # Usage example
    parser.add_argument(
        "--some_arg",
        help="desc",
        dest="arg_dest",
        required=True,
    )
    _ = parser.parse_args()


def average_team() -> None:
    """Get a player's average team."""
    parser = ArgumentParser("Average Team")
    parser.add_argument(
        "--player_id",
        help="Player ID",
        dest="player_id",
        required=True,
        type=int,
    )
    parser.add_argument(
        "--gameweek_from",
        help="Gameweek from",
        dest="gameweek_from",
        required=True,
        type=int,
    )
    parser.add_argument(
        "--gameweek_to",
        help="Gameweek to",
        dest="gameweek_to",
        required=True,
        type=int,
    )
    parser.add_argument(
        "--formation",
        help="Formation",
        dest="formation",
        required=False,
    )

    logging.basicConfig(level=logging.INFO)

    args = parser.parse_args()

    client = httpx.Client()

    player_picks = get_player_picks(
        args.player_id,
        gameweek_range=GameweekRange(
            gameweek_from=args.gameweek_from, gameweek_to=args.gameweek_to
        ),
        client=client,
    )

    player_data = get_players(get_bootstrap_data(client=client))

    if args.formation:
        formation = parse_formation(args.formation)
    else:
        formation = get_most_common_formation(
            player_picks=player_picks,
            player_data=player_data,
            client=client,
        )

    average_team = get_player_average_team(
        formation=formation,
        player_data=player_data,
        player_picks=player_picks,
        client=client,
    )

    logging.info("%s", average_team.__str__())
