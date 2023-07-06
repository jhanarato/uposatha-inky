from datetime import date

from uposatha.elements import MoonPhase

from countdown import Countdown, Appearance, IconCountMapping
from screen import ImageConfig


def test_should_report_height_for_two_rows():
    appearances = IconCountMapping[Appearance](14)
    appearances[1, 14] = Appearance(icon_size=10, max_columns=2, gap=2)

    countdown = Countdown(None, ImageConfig(), appearances,
                          date(2023, 5, 7), date(2023, 5, 10), MoonPhase.FULL)

    assert countdown.height() == 22


def test_should_report_width_for_two_rows():
    appearances = IconCountMapping[Appearance](14)
    appearances[1, 14] = Appearance(icon_size=10, max_columns=2, gap=2)

    countdown = Countdown(None, ImageConfig(), appearances,
                          date(2023, 5, 7), date(2023, 5, 10), MoonPhase.FULL)

    assert countdown.width() == 22


def test_should_report_width_for_shorter_first_row():
    appearances = IconCountMapping[Appearance](14)
    appearances[1, 14] = Appearance(icon_size=10, max_columns=3, gap=2)

    countdown = Countdown(None, ImageConfig(), appearances,
                          date(2023, 5, 7), date(2023, 5, 10), MoonPhase.FULL)

    assert countdown.width() == 34


def test_should_report_width_for_single_row():
    appearances = IconCountMapping[Appearance](14)
    appearances[1, 14] = Appearance(icon_size=10, max_columns=5, gap=2)

    countdown = Countdown(None, ImageConfig(), appearances,
                          date(2023, 5, 7), date(2023, 5, 10), MoonPhase.FULL)

    assert countdown.width() == 46
