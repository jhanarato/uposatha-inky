from datetime import date

from uposatha.elements import MoonPhase

from countdown import Countdown, Icons, GridLayout
from screen import ImageConfig


def test_should_report_height_for_two_rows():
    def resizer(icons: Icons, grid: GridLayout) -> None:
        icons.icon_size = 10
        grid._icon_size = 10
        grid._max_columns = 2
        grid._gap = 2

    countdown = Countdown(draw=None, config=ImageConfig(), resizer=resizer,
                          start=date(2023, 5, 7), end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL)

    assert countdown.height() == 22


def test_should_report_width_for_two_rows():
    def resizer(icons: Icons, grid: GridLayout) -> None:
        icons.icon_size = 10
        grid._icon_size = 10
        grid._max_columns = 2
        grid._gap = 2

    countdown = Countdown(draw=None, config=ImageConfig(), resizer=resizer,
                          start=date(2023, 5, 7), end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL)

    assert countdown.width() == 22


def test_should_report_width_for_shorter_first_row():
    def resizer(icons: Icons, grid: GridLayout) -> None:
        icons.icon_size = 10
        grid._icon_size = 10
        grid._max_columns = 3
        grid._gap = 2

    countdown = Countdown(draw=None, config=ImageConfig(), resizer=resizer,
                          start=date(2023, 5, 7), end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL)

    assert countdown.width() == 34


def test_should_report_width_for_single_row():
    def resizer(icons: Icons, grid: GridLayout) -> None:
        icons.icon_size = 10
        grid._icon_size = 10
        grid._max_columns = 5
        grid._gap = 2

    countdown = Countdown(draw=None, config=ImageConfig(), resizer=resizer,
                          start=date(2023, 5, 7), end=date(2023, 5, 10),
                          moon_phase=MoonPhase.FULL)

    assert countdown.width() == 46
