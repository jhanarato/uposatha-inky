from datetime import date, timedelta

import pytest
from uposatha.elements import MoonPhase

from countdown import Countdown, zoom_on_approach, ColumnMode, column_mode
from screen import ImageConfig

def days(number_of_days: int) -> tuple[date, date]:
    start = date(2023, 1, 1)
    end = start + timedelta(days=number_of_days - 1)
    return start, end

@pytest.mark.parametrize(
    "icons,mode",
    [
        (1, ColumnMode.THREE_ROW),
        (2, ColumnMode.THREE_ROW),
        (3, ColumnMode.THREE_ROW),
        (4, ColumnMode.THREE_ROW),
        (5, ColumnMode.THREE_ROW),
        (6, ColumnMode.THREE_ROW),
        (7, ColumnMode.THREE_ROW),
        (8, ColumnMode.THREE_ROW),
        (9, ColumnMode.THREE_ROW),
        (10, ColumnMode.THREE_ROW),
        (11, ColumnMode.THREE_ROW),
        (12, ColumnMode.THREE_ROW),
        (13, ColumnMode.THREE_ROW),
        (14, ColumnMode.THREE_ROW),
        (15, ColumnMode.THREE_ROW),
    ]
)
def test_should_calculate_fifteen_day_column_mode(icons, mode):
    assert column_mode(icons, False) == mode

@pytest.mark.parametrize(
    "icons,mode",
    [
        (1, ColumnMode.THREE_ROW),
        (2, ColumnMode.THREE_ROW),
        (3, ColumnMode.THREE_ROW),
        (4, ColumnMode.THREE_ROW),
        (5, ColumnMode.THREE_ROW),
        (6, ColumnMode.THREE_ROW),
        (7, ColumnMode.THREE_ROW),
        (8, ColumnMode.THREE_ROW),
        (9, ColumnMode.THREE_ROW),
        (10, ColumnMode.THREE_ROW),
        (11, ColumnMode.THREE_ROW),
        (12, ColumnMode.THREE_ROW),
        (13, ColumnMode.THREE_ROW),
        (14, ColumnMode.THREE_ROW),
    ]
)
def test_should_calculate_fourteen_day_column_mode(icons, mode):
    assert column_mode(icons, True) == mode
