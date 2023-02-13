from PIL import Image, ImageDraw, ImageFont
from font_fredoka_one import FredokaOne

from content import NextUposathaContent

WIDTH = 400
HEIGHT = 300

WHITE = 0
BLACK = 1
YELLOW = 2

def make_image(content: NextUposathaContent) -> Image:
    image = Image.new(mode="P", size=(WIDTH, HEIGHT), color=WHITE)

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(FredokaOne, 36)

    w, h = font.getsize(content.date)
    x = (WIDTH / 2) - (w / 2)
    y = (HEIGHT / 2) - (h / 2)

    draw.text((x, y), content.date, BLACK, font)

    return image

def text_x_value(text: str) -> int:
    pass