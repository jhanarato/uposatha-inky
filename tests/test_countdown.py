from datetime import date, timedelta

import pytest

from countdown import Countdown, CountdownLayout, distribute_centers, Icons
from content import countdown_letters
from layout import BoundingBox
from screen import ImageConfig


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

@pytest.mark.parametrize(
    "number,points",
    [
        (1, [(5, 5)]),
        (2, [(5, 5), (15, 5)]),
        (3, [(5, 5), (15, 5), (25, 5)]),
    ]
)
def test_should_calculate_center_points(number, points):
    icons = [LetterSpy(size=10) for _ in range(number)]
    box = BoundingBox(top=0, left=0, height=30, width=70)
    layout = CountdownLayout(bbox=box, icons=icons, icon_size=10, gap=0)
    assert layout._centers() == points

def test_should_center_relative_to_bbox():
    icons = [LetterSpy(size=10)]
    box = BoundingBox(top=10, left=20, height=30, width=70)
    layout = CountdownLayout(bbox=box, icons=icons, icon_size=10, gap=0)
    assert layout._centers() == [(25, 15)]

def test_should_convert_centers_to_xy():
    icons = [LetterSpy(size=10)]
    box = BoundingBox(top=0, left=0, height=30, width=70)
    layout = CountdownLayout(bbox=box, icons=icons, icon_size=10, gap=0)
    assert layout._to_xy([(5, 5), (15, 5), (25, 5)]) == [(0, 0), (10, 0), (20, 0)]

def test_should_draw_icons_at_top_left():
    icons = [
        LetterSpy(size=10),
        LetterSpy(size=10),
        LetterSpy(size=10),
    ]

    box = BoundingBox(top=0, left=0, height=100, width=100)

    layout = CountdownLayout(bbox=box, icons=icons, icon_size=10, gap=0)
    layout.draw()

    drawn_at = [icon.last_draw_at for icon in icons]
    assert drawn_at == [(0, 0), (10, 0), (20, 0)]

def test_should_create_icon_list():
    config = ImageConfig()
    letters = ["M", "T", "W"]
    icons = Icons(draw=None, config=config, icon_size=10, letters=letters)
    assert len(icons.icons) == 3

def test_should_draw_icons_with_gap():
    icons = [
        LetterSpy(size=10),
        LetterSpy(size=10),
        LetterSpy(size=10),
    ]
    bbox = BoundingBox(0, 0, 100, 100)
    layout = CountdownLayout(bbox=bbox, icons=icons, icon_size=10, gap=2)
    layout.draw()

    assert icons[0].last_draw_at == (0, 0)
    assert icons[1].last_draw_at == (12, 0)
    assert icons[2].last_draw_at == (24, 0)

@pytest.mark.parametrize(
    "number,points",
    [
        (1, [(5, 5)]),
        (2, [(5, 5), (15, 5)]),
        (3, [(5, 5), (15, 5), (25, 5)]),
    ]
)
def test_should_distribute_center_points(number, points):
    centers = distribute_centers(
        x_start=5, y_start=5, distance=10, number_of_icons=number
    )
    assert centers == points
