from PIL import ImageDraw, ImageFont

from layout import CountdownLayout, BoundingBox
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


class LetterIcon:
    def __init__(self, draw: ImageDraw, letter: str, size: int) -> None:
        self._draw = draw
        self._size = size
        self._letter = letter

        config = ImageConfig()
        self._font = config.font_styles.COUNTDOWN
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
        config = ImageConfig()

        self._draw.rectangle(
            xy=[x, y, x + self.width(), y + self.height()],
            fill=config.palette.BLACK
        )

        self._draw.text(xy=self._to_text_xy(x, y),
                        text=self._letter,
                        font=self._font,
                        fill=config.palette.WHITE)


class Countdown:
    def __init__(self, draw: ImageDraw, letters: list[str]):
        self._size = 30
        self._spacing = self._size
        self._icons = [LetterIcon(draw, letter, self._size) for letter in letters]

    def height(self) -> int:
        return self._icons[0].height()

    def width(self) -> int:
        icon_width = self._icons[0].width()
        spaces = len(self._icons) - 1
        return spaces * self._spacing + icon_width

    def draw(self, x: int, y: int) -> None:
        bbox = BoundingBox(top=y, left=x, height=self.height(), width=self.width())
        layout = CountdownLayout(bbox=bbox, icons=self._icons)
        layout.draw()
