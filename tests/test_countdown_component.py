from datetime import date

from uposatha.elements import MoonPhase

from countdown import Countdown, Appearance
from screen import ImageConfig


def test_should_report_height_for_two_rows():
    def resizer(icons: int) -> Appearance:
        return Appearance(icon_size=10, max_columns=2, gap=2)

    countdown = Countdown(draw=None, config=ImageConfig(), resizer=resizer,
                          start=date(2023, 5, 7), end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL, fourteen_day=True)

    assert countdown.height() == 22


def test_should_report_width_for_two_rows():
    def resizer(icons: int) -> Appearance:
        return Appearance(icon_size=10, max_columns=2, gap=2)

    countdown = Countdown(draw=None, config=ImageConfig(), resizer=resizer,
                          start=date(2023, 5, 7), end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL, fourteen_day=True)

    assert countdown.width() == 22


def test_should_report_width_for_shorter_first_row():
    def resizer(icons: int) -> Appearance:
        return Appearance(icon_size=10, max_columns=3, gap=2)

    countdown = Countdown(draw=None, config=ImageConfig(), resizer=resizer,
                          start=date(2023, 5, 7), end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL, fourteen_day=True)

    assert countdown.width() == 34


def test_should_report_width_for_single_row():
    def resizer(icons: int) -> Appearance:
        return Appearance(icon_size=10, max_columns=5, gap=2)

    countdown = Countdown(draw=None, config=ImageConfig(), resizer=resizer,
                          start=date(2023, 5, 7), end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL, fourteen_day=True)

    assert countdown.width() == 46
