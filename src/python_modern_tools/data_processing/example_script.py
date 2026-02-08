"""Example script using argparse CLI."""

import argparse
from collections.abc import Sequence


def echo(text: str) -> None:
    """Prints the provided text to the console."""
    print(text)


def get_parser() -> argparse.ArgumentParser:
    """Creates and returns the argument parser."""
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        "-t",
        "--text",
        required=True,
        type=str,
        help="The text to be echoed.",
    )

    return parser


def main(argv: Sequence[str] | None = None) -> None:
    """Main entry point for the script."""
    parser = get_parser()
    args = parser.parse_args(argv)

    echo(args.text)


if __name__ == "__main__":
    main()
