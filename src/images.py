from typing import List

from PIL import Image, ImageDraw, ImageFont
from font_fredoka_one import FredokaOne
from font_source_serif_pro import SourceSerifProBoldIt
from font_caladea import CaladeaBoldItalic
from font_font_awesome import FontAwesome5Free
from font_hanken_grotesk import HankenGroteskBold
from font_manrope import ManropeBold

from content import NextUposathaContent

WIDTH = 400
HEIGHT = 300

WHITE = 0
BLACK = 1
YELLOW = 2

def make_image(content: List[str]) -> Image:
    image = Image.new(mode="P", size=(WIDTH, HEIGHT), color=WHITE)
    draw = ImageDraw.Draw(image)
    draw_heading(draw, "Next Uposatha")
    draw_underline(draw)
    draw_content(draw, content)

    # draw_centered_text(image, 50, content.day)
    # draw_centered_text(image, 100, content.date)
    # draw_centered_text(image, 150, content.days_until)
    return image

def draw_heading(draw: ImageDraw, text: str) -> None:
    font = ImageFont.truetype(CaladeaBoldItalic, 40)
    x_coord = centered_x_coord(font, text)
    draw.text((x_coord, 10), text, BLACK, font)

def draw_underline(draw: ImageDraw):
    y_coord = 70
    draw.line([50, y_coord, WIDTH - 50, y_coord], BLACK, 2)

def draw_content(draw: ImageDraw, text_lines: List[str]) -> None:
    pass

def draw_centered_text(draw: ImageDraw, y_coord: int, text: str):
    font = ImageFont.truetype(FredokaOne, 36)
    text_coord = (centered_x_coord(font, text), y_coord)
    draw.text(text_coord, text, BLACK, font)


def centered_x_coord(font: ImageFont, text: str) -> int:
    w, _ = font.getsize(text)
    return (WIDTH / 2) - (w / 2)
