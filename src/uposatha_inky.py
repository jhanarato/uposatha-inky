# Script to display the uposatha on a Pimoroni Inky WHAT e-ink screen.
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
    calendar = Calendar()
    view = next_uposatha_view(calendar)
    uposatha_date = view.falls_on.strftime("%d/%m/%y")

    image = make_image(uposatha_date)
    display_on_inky(image)
    # display_on_screen(image)


if __name__ == "__main__":
    main()
