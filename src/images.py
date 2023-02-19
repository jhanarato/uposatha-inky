from typing import List

from PIL import Image, ImageDraw, ImageFont
from font_fredoka_one import FredokaOne
from font_source_serif_pro import SourceSerifProBold
from font_caladea import CaladeaBoldItalic, CaladeaBold
from font_font_awesome import FontAwesome5Free
from font_hanken_grotesk import HankenGroteskBold
from font_manrope import ManropeBold
from font_roboto import RobotoBold

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
    return image

def draw_heading(draw: ImageDraw, text: str) -> None:
    font = ImageFont.truetype(CaladeaBoldItalic, 40)
    x_coord = centered_x_coord(font, text)
    y_coord = 10
    draw.text((x_coord, y_coord), text, BLACK, font)

def draw_underline(draw: ImageDraw):
    y_coord = 70
    draw.line([50, y_coord, WIDTH - 50, y_coord], BLACK, 2)

def draw_content(draw: ImageDraw, text_lines: List[str]) -> None:
    font = ImageFont.truetype(RobotoBold, 32)
    text = "\n".join(text_lines)
    y_coord = 120
    _, _, width, _ = draw.textbbox((0,0), text, font)
    x_coord = (WIDTH / 2) - (width / 2)

    draw.multiline_text(
        xy=(x_coord, y_coord),
        text=text,
        font=font,
        fill=BLACK,
        align="center"
    )

def centered_x_coord(font: ImageFont, text: str) -> int:
    text_width = font.getlength(text)
    return (WIDTH / 2) - (text_width / 2)
