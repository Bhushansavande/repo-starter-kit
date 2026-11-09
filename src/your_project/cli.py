import argparse
import sys

from . import __version__, greet


def main(argv=None):
    parser = argparse.ArgumentParser(prog="your-project", description="Example command line tool")
    parser.add_argument("name", help="who to greet")
    parser.add_argument("--version", action="version", version=__version__)
    args = parser.parse_args(argv)
    try:
        print(greet(args.name))
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
