from collections.abc import Sequence

from PIL import ImageDraw, ImageFont

from components import Rectangle, Text
from layout import ImageComponent
from screen import ImageConfig


class Icons(Sequence):
    """ A sequence of icons representing the days until the next uposatha """
    def __init__(self,
                 draw: ImageDraw,
                 config: ImageConfig,
                 icon_size: int,
                 letters: list[str]):

        self._icon_size = icon_size
        self._icons = [
            LetterIcon(draw=draw,
                       font=config.font_styles.COUNTDOWN,
                       background=config.palette.BLACK,
                       foreground=config.palette.WHITE,
                       letter=letter,
                       size=icon_size)
            for letter in letters
        ]

    def __len__(self):
        return len(self._icons)

    def __getitem__(self, item):
        return self._icons[item]

    @property
    def icon_size(self) -> int:
        return self._icon_size


class LetterIcon:
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
