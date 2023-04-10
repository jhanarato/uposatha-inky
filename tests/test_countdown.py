from datetime import date, timedelta
from typing import Optional

import pytest

from content import countdown_letters
from layout import BoundingBox, CountdownLayout


def test_letters_fifteen():
    a_friday = date(2010, 3, 26)
    uposatha = a_friday + timedelta(14)
    expected = ["F", "S", "S", "M", "T", "W", "T",
                "F", "S", "S", "M", "T", "W", "T", "F"]
    assert countdown_letters(a_friday, uposatha) == expected

def test_letters_day_before():
    a_friday = date(2010, 3, 26)
    uposatha = date(2010, 3, 27)
    assert countdown_letters(a_friday, uposatha) == ["F", "S"]

def test_letters_on_day():
    a_friday = date(2010, 3, 26)
    uposatha = a_friday
    assert countdown_letters(a_friday, uposatha) == ["F"]


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


def test_should_layout_single_icon():
    icons = [LetterSpy(size=10)]
    box = BoundingBox(top=0, left=0, height=100, width=100)
    layout = CountdownLayout(bbox=box, icons=icons)
    layout.draw()

    assert icons[0].last_draw_at == (0, 0)

@pytest.mark.parametrize(
    "number,points",
    [
        (0, []),
        (1, [(5, 5)]),
        (2, [(5, 5), (15, 5)]),
        (3, [(5, 5), (15, 5), (25, 5)]),
    ]
)
def test_should_calculate_center_points(number, points):
    icons = [LetterSpy(size=10) for _ in range(number)]
    box = BoundingBox(top=0, left=0, height=30, width=70)
    layout = CountdownLayout(bbox=box, icons=icons)
    assert layout._centers() == points

def test_should_center_relative_to_bbox():
    icons = [LetterSpy(size=10)]
    box = BoundingBox(top=10, left=20, height=30, width=70)
    layout = CountdownLayout(bbox=box, icons=icons)
    assert layout._centers() == [(25, 15)]

def test_should_convert_centers_to_xy():
    icons = [LetterSpy(size=10)]
    box = BoundingBox(top=0, left=0, height=30, width=70)
    layout = CountdownLayout(bbox=box, icons=icons)
    assert layout._to_xy([(5, 5), (15, 5), (25, 5)]) == [(0, 0), (10, 0), (20, 0)]

def test_should_draw_icons_at_top_left():
    icons = [
        LetterSpy(size=10),
        LetterSpy(size=10),
        LetterSpy(size=10),
    ]

    box = BoundingBox(top=0, left=0, height=100, width=100)

    layout = CountdownLayout(bbox=box, icons=icons)
    layout.draw()

    drawn_at = [icon.last_draw_at for icon in icons]
    assert drawn_at == [(0, 0), (10, 0), (20, 0)]
