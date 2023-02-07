from inky import InkyWHAT
from PIL import Image, ImageDraw, ImageFont
from font_fredoka_one import FredokaOne

from uposatha.calendar import Calendar

from data import NextUposathaView, next_uposatha_view

WIDTH = 400
HEIGHT = 300

class NextUposathaDrawing:
    def __init__(self, image: Image) -> None:
        self.image = image

    def draw(self, view_data: NextUposathaView) -> None:
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype(FredokaOne, 36)
        draw.text((0,0), "Here we go", (0,0,0), font)


def screen_image() -> Image:
    return Image.new(mode="RGB",
                     size=(WIDTH, HEIGHT),
                     color=(255, 255, 255))

def inky_image() -> Image:
    return Image.new("P", (WIDTH, HEIGHT))

def display_on_screen() -> None:
    image = screen_image()
    calendar = Calendar()
    view = next_uposatha_view(calendar)
    drawing = NextUposathaDrawing(image)
    drawing.draw(view)
    image.show()

def display_on_inky() -> None:
    what = InkyWHAT('yellow')
    what.set_border(what.WHITE)

    image = inky_image()
    calendar = Calendar()
    view = next_uposatha_view(calendar)
    drawing = NextUposathaDrawing(image)
    drawing.draw(view)

    what.set_image(image)
    what.show()

if __name__ == "__main__":
    display_on_inky()
