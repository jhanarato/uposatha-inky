from typing import List
from PIL import ImageDraw, ImageFont

from layout import ImageComponent


class Text:
    def __init__(self, draw: ImageDraw, text: str, font: ImageFont, colour: int):
        self._draw = draw
        self._text = text
        self._font = font
        self._colour = colour

    def height(self) -> int:
        return self._font.getbbox(self._text)[3]

    def width(self) -> int:
        return self._font.getbbox(self._text)[2]

    def draw(self, x: int, y: int) -> None:
        self._draw.text(xy=(x, y),
                        text=self._text,
                        fill=self._colour,
                        font=self._font)

class HorizontalLine:
    def __init__(self, draw: ImageDraw, length: int, thickness: int, colour: int):
        self._draw = draw
        self._length = length
        self._thickness = thickness
        self._colour = colour

    def height(self) -> int:
        return 2

    def width(self) -> int:
        return self._length

    def draw(self, x: int, y: int):
        self._draw.line(
            xy=[(x, y), (x + self._length, y)],
            fill=self._colour,
            width=self._thickness
        )


class MultilineText:
    def __init__(self, draw: ImageDraw, text: str, font: ImageFont, colour: int):
        self._draw = draw
        self._text = text
        self._font = font
        self._colour = colour
        self._spacing = 10

    @property
    def _bbox(self) -> [int, int, int, int]:
        return self._draw.multiline_textbbox(
            xy=(0, 0),
            text=self._text,
            font=self._font
        )

    def height(self) -> int:
        return self._bbox[3]

    def width(self) -> int:
        return self._bbox[2]

    def draw(self, x: int, y: int) -> None:
        self._draw.multiline_text(
            xy=(x, y),
            text=self._text,
            fill=self._colour,
            font=self._font,
            spacing=self._spacing,
            align="center"
        )


class LetterIcon:
    def __init__(self, size: int) -> None:
        self._size = size

    def height(self) -> int:
        return self._size

    def width(self) -> int:
        return self._size

    def draw(self, x: int, y: int) -> None:
        pass


def letters_to_icons(self, letters: list[str]) -> list[LetterIcon]:
    return [LetterIcon(10) for letter in letters]


class Countdown:
    def __init__(self, icons: list[ImageComponent]):
        self._spacing = 10
        self.icons = icons

    def height(self) -> int:
        return self.icons[0].height()

    def width(self) -> int:
        icon_width = self.icons[0].width()
        spaces = len(self.icons) - 1
        return spaces * self._spacing + icon_width

    def draw(self, x: int, y: int) -> None:
        self.icons[0].draw(x, y)
