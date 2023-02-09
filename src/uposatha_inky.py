import argparse

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
    display = auto()
    display.set_border(display.WHITE)
    display.set_image(image)
    display.show()

def main():
    parser = argparse.ArgumentParser(
        prog="uposatha_inky.py",
        description="Displays lunar calendar details on Pimoroni Inky",
    )
    parser.add_argument("-t", "--test", action="store_true", default=False)
    args = parser.parse_args()

    calendar = Calendar()
    view = next_uposatha_view(calendar)
    uposatha_date = view.falls_on.strftime("%a %d/%m/%y")

    image = make_image(uposatha_date)

    if args.test:
        display_on_screen(image)
    else:
        display_on_inky(image)

if __name__ == "__main__":
    main()
