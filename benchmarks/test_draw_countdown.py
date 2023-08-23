from datetime import date

from uposatha.elements import MoonPhase

from compose import fifteen_day_appearance
from countdown import Countdown
from screen import WIDTH, HEIGHT
from viewer import DrawingViewer


def test_draw_countdown(benchmark):
    with DrawingViewer(height=HEIGHT, width=WIDTH, show=False) as draw:
        countdown = Countdown(
            fifteen_day_appearance(), date(2023, 7, 18), date(2023, 8, 1), MoonPhase.FULL
        )

        benchmark(countdown.draw, draw, 0, 0)
