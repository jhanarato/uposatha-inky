from datetime import date

from uposatha.elements import MoonPhase

from countdown import Countdown
from screen import ImageConfig


def test_should_report_height_for_two_rows():
    countdown = Countdown(draw=None, config=ImageConfig(), resizer=None,
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL,
                          icon_size=10, gap=2, max_columns=2)

    assert countdown.height() == 22


def test_should_report_width_for_two_rows():
    countdown = Countdown(draw=None, config=ImageConfig(), resizer=None,
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL,
                          icon_size=10, gap=2, max_columns=2)

    assert countdown.width() == 22


def test_should_report_width_for_shorter_first_row():
    countdown = Countdown(draw=None, config=ImageConfig(), resizer=None,
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL,
                          icon_size=10, gap=2, max_columns=3)

    assert countdown.width() == 34


def test_should_report_width_for_single_row():
    countdown = Countdown(draw=None, config=ImageConfig(), resizer=None,
                          start=date(2023, 5, 7),
                          end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL,
                          icon_size=10, gap=2, max_columns=5)

    assert countdown.width() == 46
