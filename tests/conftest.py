from datetime import date

import pytest
from uposatha.elements import MoonPhase

from countdown import Icons
from screen import ImageConfig


class LetterSpy:
    def __init__(self, size: int):
        self._size = size
        self.last_draw_at = None

    def height(self) -> int:
        return self._size

    def width(self) -> int:
        return self._size

    def draw(self, x: int, y: int) -> None:
        self.last_draw_at = (x, y)


def make_letter_spies(count: int) -> Icons:
    icons = Icons(None, ImageConfig(), 10, date(2000, 1, 1), date(2000, 1, 1), MoonPhase.FULL)
    icons._icons = [LetterSpy(10) for _ in range(count)]
    return icons
