from datetime import date

import pytest
from uposatha.elements import MoonPhase

from countdown import Countdown
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
