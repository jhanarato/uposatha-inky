from PIL import ImageDraw, ImageFont

from components import Rectangle, Text
from layout import ImageComponent
from screen import ImageConfig


class Icons:
    def __init__(self,
                 draw: ImageDraw,
                 config: ImageConfig,
                 icon_size: int,
                 letters: list[str]):

        if len(letters) < 1:
            raise ValueError("At least one letter is required")

        self._draw = draw
        self._config = config
        self._icon_size = icon_size
        self._letters = letters

    def __len__(self):
        return len(self._letters)
    
    @property
    def icon_size(self) -> int:
        return self._icon_size

    @property
    def icons(self) -> list[ImageComponent]:
        return [
            LetterIcon(draw=self._draw,
                       font=self._config.font_styles.COUNTDOWN,
                       background=self._config.palette.BLACK,
                       foreground=self._config.palette.WHITE,
                       letter=letter,
                       size=self._icon_size)
            for letter in self._letters
        ]


class LetterIcon:
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

    def height(self) -> int:
        return self._size

    def width(self) -> int:
        return self._size

    def _text_x(self, component_x: int) -> int:
        return component_x + (self.width() - self._text.width()) // 2

    def _text_y(self, component_y: int) -> int:
        return component_y + (self.height() - self._text.height()) // 2

    def draw(self, x: int, y: int) -> None:
        self._rect.draw(x, y)
        self._text.draw(self._text_x(x), self._text_y(y))
