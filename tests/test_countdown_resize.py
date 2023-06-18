from datetime import date, timedelta

import pytest
from uposatha.elements import MoonPhase

from countdown import Appearance, appearance, Icons, GridLayout, Countdown, zoom_on_approach
from screen import ImageConfig

def days(number_of_days: int) -> tuple[date, date]:
    start = date(2023, 1, 1)
    end = start + timedelta(days=number_of_days - 1)
    return start, end

@pytest.mark.parametrize(
    "days_inclusive,appears",
    [
        (15, Appearance(icon_size=30, max_columns=8, gap=4)),
        (8, Appearance(icon_size=30, max_columns=8, gap=4)),
        (7, Appearance(icon_size=40, max_columns=7, gap=4)),
        (4, Appearance(icon_size=40, max_columns=4, gap=4)),
        (3, Appearance(icon_size=50, max_columns=3, gap=4)),
        (2, Appearance(icon_size=50, max_columns=2, gap=4)),
    ]
)
def test_should_adjust_size_as_uposatha_gets_closer(days_inclusive, appears):
    start, end = days(days_inclusive)
    assert appearance(start, end) == appears

@pytest.mark.parametrize(
    "days_inclusive,icon_size",
    [
        (15, 30),
        (8, 30),
        (7, 40),
        (4, 40),
        (3, 50),
        (2, 50),
    ]
)
def test_should_increase_icon_size_as_uposatha_approaches(days_inclusive, icon_size):
    start, end = days(days_inclusive)
    icons = Icons(None, ImageConfig(), 0, start, end, MoonPhase.FULL)
    grid = GridLayout()
    zoom_on_approach(icons, grid)

    assert icons.icon_size == icon_size
    assert grid._icon_size == icon_size

def test_should_modify_icon_size_with_resizer():
    start, end = days(4)

    def resizer(icons: Icons, grid: GridLayout) -> None:
        icons.icon_size = 3
        grid.icon_size(3)

    countdown = Countdown(None, ImageConfig(), resizer, start, end, MoonPhase.FULL, 0, 0, 0)
    assert countdown.icon_size == 3
