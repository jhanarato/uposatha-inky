from datetime import date, timedelta

import pytest
from uposatha.elements import MoonPhase

from countdown import Countdown, zoom_on_approach
from screen import ImageConfig

def days(number_of_days: int) -> tuple[date, date]:
    start = date(2023, 1, 1)
    end = start + timedelta(days=number_of_days - 1)
    return start, end
