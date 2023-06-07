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

def test_should_put_gap_between_icons():
    icon_size = 10
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL,
                          icon_size=icon_size, gap=2, max_columns=2)

    spies = [LetterSpy(10) for _ in range(4)]
    countdown._grid._icons._icons = spies
    countdown.draw(0, 0)

    assert [spy.last_draw_at for spy in spies] == [
        (0, 0), (12, 0),
        (0, 12), (12, 12)
    ]


def test_should_draw_offset_from_component_coordinates():
    icon_size = 10
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL,
                          icon_size=icon_size, gap=2, max_columns=2)

    spies = [LetterSpy(10) for _ in range(4)]
    countdown._grid._icons._icons = spies
    countdown.draw(6, 9)

    assert [spy.last_draw_at for spy in spies] == [
        (6, 9), (18, 9),
        (6, 21), (18, 21)
    ]
