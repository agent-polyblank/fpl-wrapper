"""Entry point for module fpl."""

from argparse import ArgumentParser

import httpx

from fpl.analysis.analysis import get_player_average_team
from fpl.data_fetch.players import get_bootstrap_data
from fpl.input_parsing.parse_formation import parse_formation


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
    parser = ArgumentParser("average_team")
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
        required=True,
    )
    args = parser.parse_args()

    get_player_average_team(
        args.player_id,
        args.gameweek_from,
        args.gameweek_to,
        parse_formation(args.formation),
        bootstrap_data=get_bootstrap_data(client=httpx.Client()),
    )
