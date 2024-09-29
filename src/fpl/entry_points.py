"""Entry point for module fpl."""

from argparse import ArgumentParser


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
