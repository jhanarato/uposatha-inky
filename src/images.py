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
    draw_centered_text(image, 0, "Next Uposatha:")
    draw_centered_text(image, 50, content.day)
    draw_centered_text(image, 100, content.date)
    draw_centered_text(image, 150, content.days_until)
    return image

def draw_centered_text(image: Image, y_coord: int, text: str):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FredokaOne, 36)
    text_coord = (centered_x_coord(font, text), y_coord)
    draw.text(text_coord, text, BLACK, font)


def centered_x_coord(font: ImageFont, text: str) -> int:
    w, _ = font.getsize(text)
    return (WIDTH / 2) - (w / 2)
