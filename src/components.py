from PIL import ImageDraw, ImageFont
from font_roboto import RobotoBold

from screen import ScreenConfig


class Text:
    def __init__(self, imgDraw: ImageDraw, config: ScreenConfig, text: str):
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

class Underline:
    pass

class MultilineText:
    pass

class Countdown:
    pass