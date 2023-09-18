from PIL.ImageDraw import ImageDraw

from bbox import BBox
from components import Text
from fonts import Font
from layout import VerticalLayout, Align
from screen import Ink
from views import Pane


class MoonWords:
    def __init__(self, first_word: str, second_word: str, colour: Ink):
        font = Font("roboto-bold", 30)
        self._first_text = Text(first_word, font, colour)
        self._second_text = Text(second_word, font, colour)
        self._spacing = 15

    def height(self) -> int:
        h = self._first_text.height()
        h += self._second_text.height()
        h += self._spacing
        return h

    def width(self) -> int:
        return max(self._first_text.width(), self._second_text.width())

    def draw(self, draw: ImageDraw, x: int, y: int) -> None:
        components = [self._first_text, self._second_text]
        bbox = BBox(
            left=x,
            right=x + self.width(),
            top=y,
            bottom=y + self.height()
        )
        layout = VerticalLayout(bbox, Align.CENTER, self._spacing)
        pane = Pane(components, layout)
        pane.draw(draw)
