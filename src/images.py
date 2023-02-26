from typing import List, Tuple
from dataclasses import dataclass
from PIL import Image, ImageDraw, ImageFont
from font_roboto import RobotoBold

from content import NextUposatha, Countdown

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

@dataclass
class CountdownArea:
    x: int
    y: int
    width: int
    height: int
    border: int
    letter_spacing: int
    row_spacing: int

    @property
    def rectangle(self):
        return [self.x, self.y, self.x + self.width, self.y + self.height]

def draw_countdown(draw, days: List[str]):
    area = CountdownArea(
        x=30,
        y=220,
        width=340,
        height=70,
        border=10,
        letter_spacing=20,
        row_spacing=20
    )

    draw.rectangle(area.rectangle, fill=BLACK)
    draw_countdown_row(draw, days, 0, area)
    draw_countdown_row(draw, days, 1, area)

def draw_countdown_row(draw: Image,
                       row: List[str],
                       row_num: int,
                       area: CountdownArea) -> None:
    for index, day_letter in enumerate(reversed(row)):
        x_coord, y_coord = countdown_letter_xy(area, index, row_num)
        font = ImageFont.truetype(font=RobotoBold, size=20)
        draw.text(
            xy=(x_coord, y_coord),
            text=day_letter,
            font=font,
            fill=WHITE
        )

def countdown_letter_xy(area: CountdownArea,
                        letter_num: int,
                        row_num: int) -> Tuple[int, int]:
    x_coord = area.x + area.width - area.border - (area.letter_spacing * letter_num)
    y_coord = area.y + (area.row_spacing * row_num)
    return x_coord, y_coord

def centered_x_coord(object_width: int) -> int:
    return round((WIDTH / 2) - (object_width / 2))
