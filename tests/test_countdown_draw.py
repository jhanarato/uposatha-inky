from datetime import date

import pytest
from uposatha.elements import MoonPhase

from countdown import Countdown, icon_xy
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

@pytest.mark.parametrize(
    "row,column,xy",
    [
        (0, 0, (0, 0)),
        (0, 1, (10, 0)),
        (1, 0, (0, 10)),
        (1, 1, (10, 10)),
    ]
)
def test_should_distribute_icons_at_grid_positions(row, column, xy):
    assert icon_xy(
        parent_x=0, parent_y=0,
        row=row, column=column,
        gap=0, icon_size=10
    ) == xy

@pytest.mark.parametrize(
    "row,column,xy",
    [
        (0, 0, (0, 0)),
        (0, 1, (12, 0)),
        (1, 0, (0, 12)),
        (1, 1, (12, 12)),
    ]
)
def test_should_distribute_icons_with_gap(row, column, xy):
    assert icon_xy(
        parent_x=0, parent_y=0,
        row=row, column=column,
        gap=2, icon_size=10
    ) == xy

@pytest.mark.parametrize(
    "row,column,xy",
    [
        (0, 0, (6, 9)),
        (0, 1, (18, 9)),
        (1, 0, (6, 21)),
        (1, 1, (18, 21)),
    ]
)
def test_should_distribute_icons_within_parent(row, column, xy):
    assert icon_xy(
        parent_x=6, parent_y=9,
        row=row, column=column,
        gap=2, icon_size=10
    ) == xy
