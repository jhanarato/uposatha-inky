from datetime import date, timedelta

import pytest

from countdown import Countdown, Grid, skip_n, Icons
from screen import ImageConfig


def test_letters_fifteen():
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2010, 3, 26), end=date(2010, 4, 9),
                          icon_size=0, gap=0, max_columns=0)

    expected = "FSSMTWTFSSMTWTF"

    assert str(countdown) == expected

def test_letters_day_before():
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2010, 3, 26), end=date(2010, 3, 27),
                          icon_size=0, gap=0, max_columns=0)

    assert [str(icon) for icon in countdown._icons] == ["F", "S"]

def test_letters_on_day():
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2010, 3, 26), end=date(2010, 3, 26),
                          icon_size=0, gap=0, max_columns=0)

    assert [str(icon) for icon in countdown._icons] == ["F"]


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


def test_should_create_icon_list():
    config = ImageConfig()
    letters = ["M", "T", "W"]
    icons = Icons(draw=None, config=config, icon_size=10, letters=letters)
    assert len(icons) == 3

@pytest.fixture
def four_icons():
    config = ImageConfig()
    return Icons(None, config, 10, ["S", "M", "T", "W"])

def test_should_report_height_for_two_rows():
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          icon_size=10, gap=2, max_columns=2)

    assert countdown.height() == 22

def test_should_report_width_for_two_rows():
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          icon_size=10, gap=2, max_columns=2)

    assert countdown.width() == 22

def test_should_report_width_for_shorter_first_row():
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          icon_size=10, gap=2, max_columns=3)

    assert countdown.width() == 34

def test_should_report_width_for_single_row(four_icons):
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          icon_size=10, gap=2, max_columns=5)

    assert countdown.width() == 46

def make_letter_spies(count: int) -> list[LetterSpy]:
    return [LetterSpy(10) for _ in range(count)]

@pytest.mark.parametrize(
    "icon_count,max_columns,columns",
    [
        (2, 2, 2),
    ]
)
def test_grid_column_count(icon_count, max_columns, columns):
    spies = make_letter_spies(icon_count)
    grid = Grid(spies, max_columns)
    assert grid.columns == columns

def test_fewer_icons_than_columns():
    grid = Grid(make_letter_spies(3), 4)
    assert grid.columns == 3

@pytest.mark.parametrize(
    "icon_count,max_columns,rows",
    [
        (2, 3, 1),
        (4, 2, 2),
        (6, 2, 3),
    ]
)
def test_grid_row_count(icon_count, max_columns, rows):
    spies = make_letter_spies(icon_count)
    grid = Grid(spies, max_columns)
    assert grid.rows == rows

def test_should_iterate_grid_with_no_empty_positions():
    icons = Icons(None, ImageConfig(), 10, ["S", "M", "T", "W"])
    grid = Grid(icons, 2)
    rows_columns = [(pos.row, pos.column) for pos in grid]
    assert rows_columns == [
        (0, 0), (0, 1), (1, 0), (1, 1)
    ]

def test_should_iterate_grid_with_empty_positions():
    icons = Icons(None, ImageConfig(), 10, ["S", "M", "T"])
    grid = Grid(icons, 2)
    rows_columns = [(pos.row, pos.column) for pos in grid]
    assert rows_columns == [
        (0, 1), (1, 0), (1, 1)
    ]

def test_should_position_icon_in_row_and_column():
    icons = Icons(None, ImageConfig(), 10, ["S", "M", "T", "W"])
    grid = Grid(icons, 2)

    grid_str = "".join(
        [str(pos.icon) for pos in grid]
    )

    assert grid_str == "SMTW"

def test_skip_n():
    five_iter = iter([1, 2, 3, 4, 5])
    skip_n(five_iter, 3)
    assert list(five_iter) == [4, 5]

@pytest.mark.parametrize(
    "row,column,drawn_at",
    [
        (0, 0, (0, 0)),
        (0, 1, (12, 0)),
        (1, 0, (0, 12)),
        (1, 1, (12, 12)),
        (3, 3, (36, 36))
    ]
)
def test_should_draw_icon_at_grid_position(row, column, drawn_at):
    icon_size = 10
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          icon_size=icon_size, gap=2, max_columns=2)

    spy = LetterSpy(icon_size)
    countdown._draw_icon(spy, top=0, left=0, row=row, column=column)
    assert spy.last_draw_at == drawn_at

@pytest.mark.parametrize(
    "gap,drawn_at",
    [
        (0, (10, 10)),
        (1, (11, 11)),
        (2, (12, 12)),
        (3, (13, 13)),
    ]
)
def test_should_space_icons_with_gap(gap, drawn_at):
    icon_size = 10
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          icon_size=icon_size, gap=gap, max_columns=2)

    spy = LetterSpy(icon_size)
    countdown._draw_icon(spy, top=0, left=0, row=1, column=1)
    assert spy.last_draw_at == drawn_at

@pytest.mark.parametrize(
    "icon_size,drawn_at",
    [
        (1, (3, 3)),
        (2, (4, 4)),
        (3, (5, 5)),
    ]
)
def test_should_space_with_icon_size(icon_size, drawn_at):
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          icon_size=icon_size, gap=2, max_columns=2)

    spy = LetterSpy(icon_size)
    countdown._draw_icon(spy, top=0, left=0, row=1, column=1)
    assert spy.last_draw_at == drawn_at

@pytest.mark.parametrize(
    "top,left,drawn_at",
    [
        (0, 0, (12, 12)),
        (5, 7, (19, 17)),
    ]
)
def test_should_be_drawn_at_component_location(top, left, drawn_at):
    icon_size = 10
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          icon_size=icon_size, gap=2, max_columns=2)

    spy = LetterSpy(icon_size)
    countdown._draw_icon(spy, top=top, left=left, row=1, column=1)
    assert spy.last_draw_at == drawn_at
