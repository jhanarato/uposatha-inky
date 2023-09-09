import argparse
import datetime
from datetime import date

import screen
from context import get_context
from viewer import DrawingViewer
from views import select_view


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


def update(today: date):
    context = get_context(today)
    view = select_view(context)
    with DrawingViewer(width=screen.WIDTH, height=screen.HEIGHT) as draw:
        view.show(draw)


def main():
    args = parse_args()
    update(args.date)


if __name__ == "__main__":
    main()
