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
        (1, ColumnMode.ONE_ROW_LARGE_SIZE),
        (2, ColumnMode.ONE_ROW_LARGE_SIZE),
        (3, ColumnMode.ONE_ROW_LARGE_SIZE),
        (4, ColumnMode.ONE_ROW_MEDIUM_SIZE),
        (5, ColumnMode.ONE_ROW_MEDIUM_SIZE),
        (6, ColumnMode.ONE_ROW_MEDIUM_SIZE),
        (7, ColumnMode.ONE_ROW_MEDIUM_SIZE),
        (8, ColumnMode.ONE_ROW_MEDIUM_SIZE),
        (9, ColumnMode.TWO_ROW_15_DAY),
        (10, ColumnMode.TWO_ROW_15_DAY),
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
        (1, ColumnMode.ONE_ROW_LARGE_SIZE),
        (2, ColumnMode.ONE_ROW_LARGE_SIZE),
        (3, ColumnMode.ONE_ROW_LARGE_SIZE),
        (4, ColumnMode.ONE_ROW_MEDIUM_SIZE),
        (5, ColumnMode.ONE_ROW_MEDIUM_SIZE),
        (6, ColumnMode.ONE_ROW_MEDIUM_SIZE),
        (7, ColumnMode.ONE_ROW_MEDIUM_SIZE),
        (8, ColumnMode.TWO_ROW_14_DAY),
        (9, ColumnMode.TWO_ROW_14_DAY),
        (10, ColumnMode.TWO_ROW_14_DAY),
        (11, ColumnMode.TWO_ROW_14_DAY),
        (12, ColumnMode.TWO_ROW_14_DAY),
        (13, ColumnMode.TWO_ROW_14_DAY),
        (14, ColumnMode.TWO_ROW_14_DAY),
    ]
)
def test_should_calculate_fourteen_day_column_mode(icons, mode):
    assert column_mode(icons, True) == mode
