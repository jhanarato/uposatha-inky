from PIL import ImageDraw, ImageFont


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


class Rectangle:
    def __init__(self, draw: ImageDraw, height: int, width: int, colour: int):
        self._draw = draw
        self._height = height
        self._width = width
        self._colour = colour

    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return self._width

    def draw(self, x: int, y: int) -> None:
        self._draw.rectangle(
            xy=[x, y, x + self.width(), y + self.height()],
            fill=self._colour
        )


class DayOfWeekIcon:
    """ An icon displaying the abbreviated day of the week. e.g. M for Monday. """
    def __init__(self,
                 draw: ImageDraw,
                 font: ImageFont,
                 background: int,
                 foreground: int,
                 letter: str,
                 size: int) -> None:
        self._size = size
        self._rect = Rectangle(draw, self.height(), self.width(), background)
        self._text = Text(draw, letter, font, foreground)
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

    def draw(self, x: int, y: int) -> None:
        self._rect.draw(x, y)
        self._text.draw(self._text_x(x), self._text_y(y))

    def __str__(self):
        return self.letter

class BlankIcon:
    """ Placeholder that takes up space but draws nothing"""
    def __init__(self, size: int):
        self._size = size

    def height(self) -> int:
        return self._size

    def width(self) -> int:
        return self._size

    def draw(self, x: int, y: int) -> None:
        pass

    def __str__(self):
        return " "
