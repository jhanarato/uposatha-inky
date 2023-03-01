from collections.abc import Iterator
from typing import List, Tuple
from dataclasses import dataclass
from PIL import Image, ImageDraw, ImageFont
from font_roboto import RobotoBold

from content import NextUposatha

WIDTH = 400
HEIGHT = 300

WHITE = 0
BLACK = 1
YELLOW = 2

def make_image(content: NextUposatha) -> Image:
    image = Image.new(mode="P", size=(WIDTH, HEIGHT), color=WHITE)
    draw = ImageDraw.Draw(image)
    draw_heading(draw, "Uposatha")
    draw_underline(draw, y_coord=70)
    draw_info(draw, content.info)
    draw_countdown(draw, content.countdown)
    return image

def draw_heading(draw: ImageDraw, text: str) -> None:
    font = ImageFont.truetype(font=RobotoBold, size=36)
    x_coord = centered_x_coord(font.getlength(text))
    y_coord = 10
    draw.text((x_coord, y_coord), text, BLACK, font)

def draw_underline(draw: ImageDraw, y_coord: int):
    draw.line([50, y_coord, WIDTH - 50, y_coord], BLACK, 2)

def draw_info(draw: ImageDraw, text: str) -> None:
    font = ImageFont.truetype(font=RobotoBold, size=32)
    y_coord = 90
    width = draw.textbbox((0,0), text, font)[2]
    x_coord = centered_x_coord(width)

    draw.multiline_text(
        xy=(x_coord, y_coord),
        text=text,
        font=font,
        fill=BLACK,
        align="center",
        spacing=10
    )

def draw_countdown(draw: Image, letters: List[str]) -> None:
    centres = centre_points(
        y_coord=220,
        screen_width=WIDTH,
        spacing=20,
        number_of_points=len(letters)
    )

    for letter, centre in zip(letters, centres):
        draw_letter(draw, letter, centre)

def draw_letter(draw: Image, letter: str, centre: Tuple[int, int]):
    font = ImageFont.truetype(font=RobotoBold, size=20)
    draw.text(
        xy=centre,
        text=letter,
        font=font,
        fill=BLACK
    )

def centered_x_coord(object_width: int) -> int:
    return round((WIDTH / 2) - (object_width / 2))

def centre_points(y_coord: int,
                  screen_width: int,
                  spacing: int,
                  number_of_points: int) -> List[Tuple[int, int]]:

    points_width = (number_of_points - 1) * spacing
    left = (screen_width - points_width) / 2

    points = []
    for point_num in range(number_of_points):
        x_coord = int(left + (point_num * spacing))
        points.append((x_coord, y_coord))
    return points
