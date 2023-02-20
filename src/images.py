from typing import List

from PIL import Image, ImageDraw, ImageFont
from font_roboto import RobotoBold

WIDTH = 400
HEIGHT = 300

WHITE = 0
BLACK = 1
YELLOW = 2

def make_image(content: str) -> Image:
    image = Image.new(mode="P", size=(WIDTH, HEIGHT), color=WHITE)
    draw = ImageDraw.Draw(image)
    draw_heading(draw, "Uposatha")
    draw_underline(draw)
    draw_content(draw, content)
    return image

def draw_heading(draw: ImageDraw, text: str) -> None:
    font = ImageFont.truetype(font=RobotoBold, size=36)
    x_coord = centered_x_coord(font, text)
    y_coord = 10
    draw.text((x_coord, y_coord), text, BLACK, font)

def draw_underline(draw: ImageDraw):
    y_coord = 70
    draw.line([50, y_coord, WIDTH - 50, y_coord], BLACK, 2)

def draw_content(draw: ImageDraw, text: str) -> None:
    font = ImageFont.truetype(font=RobotoBold,
                              size=32)
    y_coord = 120
    _, _, width, _ = draw.textbbox((0,0), text, font)
    x_coord = (WIDTH / 2) - (width / 2)

    draw.multiline_text(
        xy=(x_coord, y_coord),
        text=text,
        font=font,
        fill=BLACK,
        align="center",
        spacing=20
    )

def centered_x_coord(font: ImageFont, text: str) -> int:
    text_width = font.getlength(text)
    return (WIDTH / 2) - (text_width / 2)
