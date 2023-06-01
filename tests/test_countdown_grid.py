import pytest
from uposatha.elements import MoonPhase

from conftest import make_letter_spies
from countdown import Grid, Icons
from screen import ImageConfig


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
