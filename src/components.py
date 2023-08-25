from typing import Protocol

from PIL import ImageDraw

from fonts import Font
from glyph_metrics import glyph_metrics
from screen import Ink


class Drawable(Protocol):
    def draw(self, draw: ImageDraw, x: int, y: int) -> None: ...

    """ Draw given the top left coordinates """


class Text:
    def __init__(self, text: str, font: Font, colour: Ink):
        self._text = text
        self._font = font
        self._colour = colour

    def height(self) -> int:
        return self._font.height(self._text)

    def width(self) -> int:
        return self._font.width(self._text)

    def draw(self, draw: ImageDraw, x: int, y: int) -> None:
        draw.text(xy=(x, y),
                  text=self._text,
                  fill=self._colour.value,
                  font=self._font.as_pillow())


class Glyph:
    def __init__(self, char: str, font: Font, colour: Ink):
        self._font = font
        self._char = char
        self._colour = colour
        self._metrics = glyph_metrics(self._font.path, self._char)

    def width(self) -> int:
        return self._metrics.width.to_pixels(self._font.size)

    def height(self) -> int:
        return self._metrics.height.to_pixels(self._font.size)

    def relative_x(self, x: int) -> int:
        x_min = self._metrics.x_min.to_pixels(self._font.size)
        return x - x_min

    def relative_y(self, y: int) -> int:
        ascent = self._font.ascent()
        above_baseline = self._metrics.y_max.to_pixels(self._font.size)
        distance_to_glyph_top = ascent - above_baseline
        return y - distance_to_glyph_top

    def draw(self, draw: ImageDraw, x: int, y: int):
        draw.text(xy=(self.relative_x(x), self.relative_y(y)),
                  text=self._char,
                  fill=self._colour.value,
                  font=self._font.as_pillow())


class HorizontalLine:
    def __init__(self, length: int, colour: Ink):
        self._length = length
        self._colour = colour

    def height(self) -> int:
        return 2

    def width(self) -> int:
        return self._length

    def draw(self, draw: ImageDraw, x: int, y: int):
        draw.line(
            xy=[(x, y), (x + self._length, y)],
            fill=self._colour.value,
            width=2
        )


class Rectangle:
    def __init__(self, height: int, width: int, colour: Ink):
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
            fill=self._colour.value
        )


class Circle:
    def __init__(self, diameter: int, fill: Ink, outline: Ink):
        self._diameter = diameter
        self._fill = fill
        self._outline = outline

    def height(self) -> int:
        return self._diameter

    def width(self) -> int:
        return self._diameter

    def draw(self, draw: ImageDraw, x: int, y: int) -> None:
        draw.ellipse(
            xy=[(x, y), (x + self.width(), y + self.height())],
            fill=self._fill.value,
            outline=self._outline.value,
            width=3
        )


class DayOfWeekIcon:
    """
    An icon displaying the abbreviated day of the week. e.g. M for Monday.
    """

    def __init__(self, letter: str, size: int) -> None:
        self._letter = letter
        self._size = size
        self._circle = Circle(self._size, fill=Ink.WHITE, outline=Ink.BLACK)
        font = Font("roboto-bold", round(self._size * 0.7))
        self._glyph = Glyph(letter, font, Ink.BLACK)

    def height(self) -> int:
        return self._size

    def width(self) -> int:
        return self._size

    @property
    def letter(self):
        return self._letter

    def draw(self, draw: ImageDraw, x: int, y: int) -> None:
        self._circle.draw(draw, x, y)
        glyph_x = x + round((self.width() / 2) - (self._glyph.width() / 2))
        glyph_y = y + round((self.height() / 2) - (self._glyph.height() / 2))
        self._glyph.draw(draw, glyph_x, glyph_y)

    def __str__(self):
        return self.letter


class FullMoonIcon:
    def __init__(self, size: int):
        self._size = size

    def height(self) -> int:
        return self._size

    def width(self) -> int:
        return self._size

    def draw(self, draw: ImageDraw, x: int, y: int) -> None:
        circle = Circle(self._size, fill=Ink.YELLOW, outline=Ink.BLACK)
        circle.draw(draw, x, y)

    def __str__(self):
        return "*"


class NewMoonIcon:
    def __init__(self, size: int):
        self._size = size

    def height(self) -> int:
        return self._size

    def width(self) -> int:
        return self._size

    def draw(self, draw: ImageDraw, x: int, y: int) -> None:
        circle = Circle(self._size, fill=Ink.BLACK, outline=Ink.BLACK)
        circle.draw(draw, x, y)

    def __str__(self):
        return "O"
