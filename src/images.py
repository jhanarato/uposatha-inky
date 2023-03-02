from typing import List, Tuple
from dataclasses import dataclass
from PIL import Image, ImageDraw, ImageFont
from font_roboto import RobotoBold

from content import NextUposatha

@dataclass(frozen=True)
class DrawingConfig:
    height: int = 300
    width:  int = 400
    white:  int = 0
    black:  int = 1
    yellow: int = 2

def make_image(content: NextUposatha) -> Image:
    config = DrawingConfig()
    image = Image.new(mode="P", size=(config.width, config.height), color=config.white)
    draw = ImageDraw.Draw(image)
    draw_heading(draw, config ,"Uposatha")
    draw_underline(draw, config, y_coord=70)
    draw_info(draw, config, content.info)
    draw_countdown(draw, config, content.countdown)
    return image

def draw_heading(draw: ImageDraw, config: DrawingConfig, text: str) -> None:
    font = ImageFont.truetype(font=RobotoBold, size=36)
    x_coord = centered_x_coord(config.width, font.getlength(text))
    y_coord = 10
    draw.text((x_coord, y_coord), text, config.black, font)

def draw_underline(draw: ImageDraw, config: DrawingConfig, y_coord: int):
    draw.line([50, y_coord, config.width - 50, y_coord], config.black, 2)

def draw_info(draw: ImageDraw, config: DrawingConfig, text: str) -> None:
    font = ImageFont.truetype(font=RobotoBold, size=32)
    y_coord = 90
    text_width = draw.textbbox((0,0), text, font)[2]
    x_coord = centered_x_coord(config.width, text_width)

    draw.multiline_text(
        xy=(x_coord, y_coord),
        text=text,
        font=font,
        fill=config.black,
        align="center",
        spacing=10
    )

def draw_countdown(draw: Image, config: DrawingConfig, letters: List[str]) -> None:
    centres = centre_points(
        y_coord=220,
        screen_width=config.width,
        spacing=20,
        number_of_points=len(letters)
    )

    for letter, centre in zip(letters, centres):
        draw_letter(draw, config.black, letter, centre)

def draw_letter(draw: Image, colour: int, letter: str, centre: Tuple[int, int]):
    font = ImageFont.truetype(font=RobotoBold, size=20)
    draw.text(
        xy=centre,
        text=letter,
        font=font,
        fill=colour
    )

def centered_x_coord(screen_width: int, object_width: int) -> int:
    return round((screen_width / 2) - (object_width / 2))

def centre_points(y_coord: int,
                  screen_width: int,
                  spacing: int,
                  number_of_points: int) -> List[Tuple[int, int]]:

    points_width = (number_of_points - 1) * spacing
    left = (screen_width - points_width) / 2

    return [(int(left + (point_number * spacing)), y_coord)
            for point_number in range(number_of_points)]
