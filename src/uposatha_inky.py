import argparse

import datetime

from content import next_uposatha_content
from compose import next_uposatha


def parse_args():
    parser = argparse.ArgumentParser(
        prog="uposatha_inky.py",
        description="Displays lunar calendar details on Pimoroni Inky",
    )
    parser.add_argument("-d", "--date",
                        type=datetime.date.fromisoformat,
                        default=datetime.date.today(),
                        help="Set today's date. Defaults to system date.")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    content = next_uposatha_content(args.date)
    next_uposatha(content)


if __name__ == "__main__":
    main()
