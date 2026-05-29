"""Command line interface for the addition calculator."""

import argparse

from add_calculator import add


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Add two numbers.")
    parser.add_argument("left", type=float, help="First number")
    parser.add_argument("right", type=float, help="Second number")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    print(add(args.left, args.right))


if __name__ == "__main__":
    main()
