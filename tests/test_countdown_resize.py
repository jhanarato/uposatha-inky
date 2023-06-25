from datetime import date, timedelta

import pytest
from uposatha.elements import MoonPhase

from countdown import Countdown, Icons, GridLayout, zoom_on_approach, Appearance
from screen import ImageConfig

def days(number_of_days: int) -> tuple[date, date]:
    start = date(2023, 1, 1)
    end = start + timedelta(days=number_of_days - 1)
    return start, end

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
    appearance = zoom_on_approach(days_inclusive)
    assert appearance.icon_size == icon_size

def test_should_adjust_columns_while_zooming():
    countdown = Countdown(draw=None, config=ImageConfig(), resizer=zoom_on_approach,
                          start=date(2023, 5, 7), end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL)

    assert countdown._layout.columns == 4
