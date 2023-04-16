from PIL import ImageDraw, ImageFont

from layout import CountdownLayout, BoundingBox, ImageComponent
from screen import ImageConfig


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

class LetterIcon:
    def __init__(self,
                 draw: ImageDraw,
                 font: ImageFont,
                 background: int,
                 foreground: int,
                 letter: str, size: int) -> None:
        self._draw = draw
        self._size = size
        self._letter = letter

        self._font = font
        self._background = background
        self._foreground = foreground

        self._text_width = self._font.getbbox(self._letter)[2]
        self._text_height = self._font.getbbox(self._letter)[3]

    def _text_x_offset(self) -> int:
        return (self.width() - self._text_width) // 2

    def _text_y_offset(self) -> int:
        return (self.height() - self._text_height) // 2

    def _to_text_xy(self, icon_x: int, icon_y: int) -> tuple[int, int]:
        x = icon_x + self._text_x_offset()
        y = icon_y + self._text_y_offset()
        return x, y

    def height(self) -> int:
        return self._size

    def width(self) -> int:
        return self._size

    def draw(self, x: int, y: int) -> None:
        rect = Rectangle(draw=self._draw,
                         height=self.height(),
                         width=self.width(),
                         colour=self._background)

        rect.draw(x, y)

        text = Text(draw=self._draw,
                    text=self._letter,
                    font=self._font,
                    colour=self._foreground)

        text.draw(*self._to_text_xy(x, y))

def create_icons(draw: ImageDraw,
                 config: ImageConfig,
                 size: int,
                 letters: list[str]) -> list[LetterIcon]:
    return [
        LetterIcon(draw=draw,
                   font=config.font_styles.COUNTDOWN,
                   background=config.palette.BLACK,
                   foreground=config.palette.WHITE,
                   letter=letter,
                   size=size)
        for letter in letters
    ]


class Countdown:
    def __init__(self, icons: list[ImageComponent]):
        self._icons = icons
        self._gap = 2

    def _spacing(self) -> int:
        return max(self._icons, key=lambda icon: icon.width()).width() + self._gap

    def height(self) -> int:
        return self._icons[0].height()

    def width(self) -> int:
        icon_width = self._icons[0].width()
        spaces = len(self._icons) - 1
        return spaces * self._spacing() + icon_width

    def draw(self, x: int, y: int) -> None:
        bbox = BoundingBox(top=y, left=x, height=self.height(), width=self.width())
        layout = CountdownLayout(bbox=bbox, icons=self._icons, gap=self._gap)
        layout.draw()
