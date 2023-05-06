from datetime import date, timedelta

import pytest

from countdown import Countdown, CountdownLayout, distribute_centers, seq_to_rows
from icons import CountdownIcons
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


@pytest.fixture
def one_icon_sequence():
    config = ImageConfig()
    icon_size = 10
    icon_spies = [LetterSpy(size=10)]
    icons = CountdownIcons(None, config, icon_size, [])
    icons._icons = icon_spies
    return icons

@pytest.fixture
def three_icon_sequence():
    config = ImageConfig()
    icon_size = 10
    icon_spies = [
        LetterSpy(size=10),
        LetterSpy(size=10),
        LetterSpy(size=10),
    ]
    icons = CountdownIcons(None, config, icon_size, [])
    icons._icons = icon_spies
    return icons

@pytest.mark.parametrize(
    "number,points",
    [
        (1, [(5, 5)]),
        (2, [(5, 5), (15, 5)]),
        (3, [(5, 5), (15, 5), (25, 5)]),
    ]
)
def test_should_calculate_center_points(number, points):
    config = ImageConfig()
    icon_size = 10
    icon_spies = [LetterSpy(size=icon_size) for _ in range(number)]
    icons = CountdownIcons(None, config, icon_size, [])
    icons._icons = icon_spies

    box = BoundingBox(top=0, left=0, height=30, width=70)
    layout = CountdownLayout(bbox=box, icons=icons, gap=0)
    assert layout._centers() == points

def test_should_center_relative_to_bbox(one_icon_sequence):
    box = BoundingBox(top=10, left=20, height=30, width=70)
    layout = CountdownLayout(bbox=box, icons=one_icon_sequence, gap=0)
    assert layout._centers() == [(25, 15)]

def test_should_convert_centers_to_xy(one_icon_sequence):
    box = BoundingBox(top=0, left=0, height=30, width=70)
    layout = CountdownLayout(bbox=box, icons=one_icon_sequence, gap=0)
    assert layout._to_xy([(5, 5), (15, 5), (25, 5)]) == [(0, 0), (10, 0), (20, 0)]

def test_should_draw_icons_at_top_left(three_icon_sequence):
    box = BoundingBox(top=0, left=0, height=100, width=100)

    layout = CountdownLayout(bbox=box, icons=three_icon_sequence, gap=0)
    layout.draw()

    drawn_at = [icon.last_draw_at for icon in three_icon_sequence]
    assert drawn_at == [(0, 0), (10, 0), (20, 0)]

def test_should_create_icon_list():
    config = ImageConfig()
    letters = ["M", "T", "W"]
    icons = CountdownIcons(draw=None, config=config, icon_size=10, letters=letters)
    assert len(icons) == 3

def test_should_draw_icons_with_gap(three_icon_sequence):
    bbox = BoundingBox(0, 0, 100, 100)
    layout = CountdownLayout(bbox=bbox, icons=three_icon_sequence, gap=2)
    layout.draw()

    assert three_icon_sequence[0].last_draw_at == (0, 0)
    assert three_icon_sequence[1].last_draw_at == (12, 0)
    assert three_icon_sequence[2].last_draw_at == (24, 0)

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

def test_should_split_sequence_into_two_rows():
    result = seq_to_rows(seq=[1, 2, 3, 4], row_length=2)
    assert result == [[1, 2], [3, 4]]

def test_should_split_sequence_with_smaller_first_row():
    result = seq_to_rows(seq=[1, 2, 3], row_length=2)
    assert result == [[1], [2, 3]]

def test_should_handle_sequence_equal_to_row_length():
    result = seq_to_rows(seq=[1, 2, 3], row_length=3)
    assert result == [[1, 2, 3]]

def test_should_handle_sequence_smaller_than_row_length():
    result = seq_to_rows(seq=[1, 2, 3], row_length=4)
    assert result == [[1, 2, 3]]

def test_should_split_rows_if_sequence_is_icons():
    config = ImageConfig()
    icons = CountdownIcons(None, config, 10, ["S", "M", "T", "W"])
    rows = seq_to_rows(seq=icons, row_length=3)
    assert len(rows[0]) == 1
    assert len(rows[1]) == 3

def test_should_report_height_for_two_rows():
    config = ImageConfig()
    icons = CountdownIcons(None, config, 10, ["S", "M", "T", "W"])
    countdown = Countdown(icons=icons, gap=2)
    assert countdown.height() == 22
