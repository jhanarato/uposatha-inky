from datetime import date

import pytest

from uposatha.elements import MoonPhase

from countdown import Countdown, Grid, Icons, Appearance, appearance
from screen import ImageConfig


@pytest.mark.parametrize(
    "start,end,seq",
    [
        (date(2010, 3, 26), date(2010, 4, 9), "FSSMTWTFSSMTWT*"),
        (date(2010, 3, 26), date(2010, 3, 27), "F*"),
        (date(2010, 3, 26), date(2010, 3, 26), "*"),
    ]
)
def test_letters(start, end, seq):
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2010, 3, 26), end=date(2010, 4, 9),
                          moon_phase=MoonPhase.FULL,
                          icon_size=0, gap=0, max_columns=0)

    assert str(countdown) == "FSSMTWTFSSMTWT*"

def test_should_report_height_for_two_rows():
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL,
                          icon_size=10, gap=2, max_columns=2)

    assert countdown.height() == 22

def test_should_report_width_for_two_rows():
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL,
                          icon_size=10, gap=2, max_columns=2)

    assert countdown.width() == 22

def test_should_report_width_for_shorter_first_row():
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL,
                          icon_size=10, gap=2, max_columns=3)

    assert countdown.width() == 34

def test_should_report_width_for_single_row():
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL,
                          icon_size=10, gap=2, max_columns=5)

    assert countdown.width() == 46

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
    icons = Icons(None, ImageConfig(), 10, [], MoonPhase.FULL)
    icons._icons = [LetterSpy(10) for _ in range(count)]
    return icons

@pytest.mark.parametrize(
    "icon_count,max_columns,columns",
    [
        (2, 2, 2),
        (3, 4, 3),
        (3, 5, 3),
    ]
)
def test_grid_column_count(icon_count, max_columns, columns):
    spies = make_letter_spies(icon_count)
    grid = Grid(spies, max_columns)
    assert grid.columns == columns

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

def test_should_arrange_grid_without_blanks():
    icons = Icons(None, ImageConfig(), 10, ["S", "M", "T"], MoonPhase.FULL)
    grid = Grid(icons, 2)
    contents = [(str(pos[0]), pos[1], pos[2]) for pos in grid]
    assert contents == [
        ("S", 0, 0),
        ("M", 0, 1),
        ("T", 1, 0),
        ("*", 1, 1)
    ]

def test_should_arrange_grid_with_blanks():
    icons = Icons(None, ImageConfig(), 10, ["M", "T"], MoonPhase.FULL)
    grid = Grid(icons, 2)
    contents = [(str(pos[0]), pos[1], pos[2]) for pos in grid]
    assert contents == [
        (" ", 0, 0),
        ("M", 0, 1),
        ("T", 1, 0),
        ("*", 1, 1)
    ]

def test_should_draw_icons():
    icon_size = 10
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL,
                          icon_size=icon_size, gap=0, max_columns=2)

    spies = [LetterSpy(10) for _ in range(4)]
    countdown._grid._icons._icons = spies
    countdown.draw(0, 0)

    assert [spy.last_draw_at for spy in spies] == [
        (0, 0), (10, 0),
        (0, 10), (10, 10)
    ]

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

def test_should_show_new_moon_phase():
    icons = Icons(None, ImageConfig(), 10, ["M", "T"], MoonPhase.NEW)
    grid = Grid(icons, 2)
    contents = [(str(pos[0]), pos[1], pos[2]) for pos in grid]
    assert contents == [
        (" ", 0, 0),
        ("M", 0, 1),
        ("T", 1, 0),
        ("O", 1, 1)
    ]

@pytest.mark.parametrize(
    "days_inclusive,appears",
    [
        (15, Appearance(icon_size=20, max_columns=8, gap=4)),
        (8, Appearance(icon_size=20, max_columns=8, gap=4)),
        (7, Appearance(icon_size=40, max_columns=7, gap=4)),
        (4, Appearance(icon_size=40, max_columns=4, gap=4)),
        (3, Appearance(icon_size=80, max_columns=3, gap=4)),
    ]
)
def test_should_adjust_size_as_uposatha_gets_closer(days_inclusive, appears):
    assert appearance(date(2023, 1, 1), date(2023, 1, days_inclusive)) == appears

