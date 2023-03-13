from typing import List, Tuple
from dataclasses import dataclass
from PIL import Image, ImageDraw, ImageFont
from font_roboto import RobotoBold

from content import NextUposatha
from layout import Layout, ImageComponent, Align


@dataclass(frozen=True)
class DrawingConfig:
    height: int = 300
    width:  int = 400
    white:  int = 0
    black:  int = 1
    yellow: int = 2


class TextComponent(ImageComponent):
    def __init__(self, imgDraw: ImageDraw, config: DrawingConfig, text: str):
        self._draw = imgDraw
        self._text = text
        self._font = ImageFont.truetype(font=RobotoBold, size=36)
        self._colour = config.black

    def height(self) -> int:
        return self._font.getbbox(self._text)[3]

    def width(self) -> int:
        return self._font.getbbox(self._text)[2]

    def draw(self, x: int, y: int) -> None:
        self._draw.text(xy=(x, y),
                        text=self._text,
                        fill=self._colour,
                        font=self._font)


class NextUposathaDrawing:
    def __init__(self, content: NextUposatha):
        self.config: DrawingConfig = DrawingConfig()
        self._image: Image = Image.new(mode="P",
                                      size=(self.config.width, self.config.height),
                                      color=self.config.white)
        self._draw: ImageDraw = ImageDraw.Draw(self._image)
        self.draw_heading(text="Uposatha")
        self.draw_underline(y_coord=70)
        self.draw_info(content.info)
        self.draw_countdown(content.countdown)

    @property
    def image(self):
        return self._image

    def draw_heading(self, text: str) -> None:
        component = TextComponent(self._draw, self.config, text)

        layout = Layout(screen_height=self.config.height,
                        screen_width=self.config.width)
        layout.add(component, Align.CENTRE)
        layout.draw()

    def draw_underline(self, y_coord: int):
        coords = [50, y_coord, self.config.width - 50, y_coord]
        self._draw.line(xy=coords,
                        fill=self.config.black,
                        width=2)

    def draw_info(self, text: str) -> None:
        font = ImageFont.truetype(font=RobotoBold, size=32)
        y_coord = 90
        text_width = self._draw.textbbox((0, 0), text, font)[2]
        x_coord = round((self.config.width / 2) - (text_width / 2))

        self._draw.multiline_text(
            xy=(x_coord, y_coord),
            text=text,
            font=font,
            fill=self.config.black,
            align="center",
            spacing=10
        )

    def draw_countdown(self, letters: List[str]) -> None:
        centres = centre_points(
            y_coord=220,
            screen_width=self.config.width,
            spacing=20,
            number_of_points=len(letters)
        )

        for letter, centre in zip(letters, centres):
            self.draw_letter(letter, centre)

    def draw_letter(self, letter: str, centre: Tuple[int, int]):
        font = ImageFont.truetype(font=RobotoBold, size=20)
        self._draw.text(
            xy=centre,
            text=letter,
            font=font,
            fill=self.config.black
        )


def centre_points(y_coord: int,
                  screen_width: int,
                  spacing: int,
                  number_of_points: int) -> List[Tuple[int, int]]:

    points_width = (number_of_points - 1) * spacing
    left = (screen_width - points_width) / 2

    return [(round(left + (point_number * spacing)), y_coord)
            for point_number in range(number_of_points)]
