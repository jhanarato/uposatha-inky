import argparse
import datetime

from PIL import Image
from inky import auto

from uposatha.calendar import Calendar
from data import next_uposatha_view
from graphics import make_image

def display_on_screen(image: Image) -> None:
    palette = [
        255, 255, 255, # 1 = WHITE
        0, 0, 0,       # 2 = BLACK
        255, 255, 0    # 3 = YELLOW
    ]
    image.putpalette(palette)
    converted = image.convert(mode="RGB")
    converted.show()


def display_on_inky(image: Image) -> None:
    try:
        display = auto()
    except RuntimeError:
        print("Not running with InkyWHAT e-ink display. Use --testing for screen display.")
        exit(1)

    display.set_border(display.WHITE)
    display.set_image(image)
    display.show()

def parse_args():
    parser = argparse.ArgumentParser(
        prog="uposatha_inky.py",
        description="Displays lunar calendar details on Pimoroni Inky",
    )
    parser.add_argument("-s", "--screen",
                        action="store_true",
                        default=False,
                        help="Display on screen")
    parser.add_argument("-d", "--date",
                        type=datetime.date.fromisoformat,
                        default=datetime.date.today(),
                        help="Set today's date. Defaults to system date.")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    calendar = Calendar()
    view = next_uposatha_view(calendar, args.date)
    uposatha_date = view.falls_on.strftime("%a %d/%m/%y")

    image = make_image(uposatha_date)

    if args.screen:
        display_on_screen(image)
    else:
        display_on_inky(image)


if __name__ == "__main__":
    main()
