from components import Text
from fonts import Font
from screen import Ink


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
