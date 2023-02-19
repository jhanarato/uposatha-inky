import argparse
import datetime

from PIL import Image
from inky import auto

from content import next_uposatha_content
from images import make_image

def inky_available() -> bool:
    try:
        # auto() will throw a RuntimeError if the
        # InkyWHAT is not available.
        display = auto()
        return True
    except RuntimeError:
        return False

def display_on_screen(image: Image) -> None:
    palette = [
        255, 255, 255, # 0 = WHITE
        0, 0, 0,       # 1 = BLACK
        255, 255, 0    # 2 = YELLOW
    ]
    image.putpalette(palette)
    converted = image.convert(mode="RGB")
    converted.show()

def display_on_inky(image: Image) -> None:
    display = auto()
    display.set_border(display.WHITE)
    display.set_image(image)
    display.show()

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
    image = make_image(content)

    if inky_available():
        display_on_inky(image)
    else:
        display_on_screen(image)

if __name__ == "__main__":
    main()
