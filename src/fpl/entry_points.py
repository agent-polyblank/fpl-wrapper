"""Entry point for module fpl."""

from argparse import ArgumentParser

from fpl.example import greeting


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
    args = parser.parse_args()
    greeting(args.greeting)
