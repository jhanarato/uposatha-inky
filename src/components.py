from typing import Protocol

from PIL import ImageDraw, ImageFont

class Drawable(Protocol):
    def draw(self, draw: ImageDraw, x: int, y: int) -> None: ...
    """ Draw given the top left coordinates """

class Text:
    def __init__(self, text: str, font: ImageFont, colour: int):
        self._text = text
        self._font = font
        self._colour = colour

    def height(self) -> int:
        return self._font.getbbox(self._text)[3]

    def width(self) -> int:
        return self._font.getbbox(self._text)[2]

    def draw(self, draw: ImageDraw, x: int, y: int) -> None:
        draw.text(xy=(x, y),
                  text=self._text,
                  fill=self._colour,
                  font=self._font)

class HorizontalLine:
    def __init__(self, length: int, thickness: int, colour: int):
        self._length = length
        self._thickness = thickness
        self._colour = colour

    def height(self) -> int:
        return 2

    def width(self) -> int:
        return self._length

    def draw(self, draw: ImageDraw, x: int, y: int):
        draw.line(
            xy=[(x, y), (x + self._length, y)],
            fill=self._colour,
            width=self._thickness
        )


class Rectangle:
    def __init__(self, height: int, width: int, colour: int):
        self._height = height
        self._width = width
        self._colour = colour

    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return self._width

    def draw(self, draw: ImageDraw, x: int, y: int) -> None:
        draw.rectangle(
            xy=[x, y, x + self.width(), y + self.height()],
            fill=self._colour
        )


class DayOfWeekIcon:
    """ An icon displaying the abbreviated day of the week. e.g. M for Monday. """
    def __init__(self,
                 font: ImageFont,
                 background: int,
                 foreground: int,
                 letter: str,
                 size: int) -> None:
        self._size = size
        self._rect = Rectangle(self.height(), self.width(), background)
        self._text = Text(letter, font, foreground)
        self._letter = letter

    def height(self) -> int:
        return self._size

    def width(self) -> int:
        return self._size

    @property
    def letter(self):
        return self._letter

    def _text_x(self, component_x: int) -> int:
        return component_x + (self.width() - self._text.width()) // 2

    def _text_y(self, component_y: int) -> int:
        return component_y + (self.height() - self._text.height()) // 2

    def draw(self, draw: ImageDraw, x: int, y: int) -> None:
        self._rect.draw(draw, x, y)
        self._text.draw(draw, self._text_x(x), self._text_y(y))

    def __str__(self):
        return self.letter


class FullMoonIcon:
    def __init__(self,
                 size: int,
                 fill: int,
                 outline: int,
                 ):
        self._size = size
        self._fill = fill
        self._outline = outline

    def height(self) -> int:
        return self._size

    def width(self) -> int:
        return self._size

    def draw(self, draw: ImageDraw, x: int, y: int) -> None:
        draw.ellipse(
            xy=[(x, y), (x + self.width(), y + self.height())],
            fill=self._fill,
            outline=self._outline,
            width=2
        )

    def __str__(self):
        return "*"

class NewMoonIcon:
    def __init__(self,
                 size: int,
                 fill: int):
        self._size = size
        self._fill = fill

    def height(self) -> int:
        return self._size

    def width(self) -> int:
        return self._size

    def draw(self, draw: ImageDraw, x: int, y: int) -> None:
        draw.ellipse(
            xy=[(x, y), (x + self.width(), y + self.height())],
            fill=self._fill,
            width=2
        )

    def __str__(self):
        return "O"
