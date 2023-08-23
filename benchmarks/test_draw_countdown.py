from datetime import date

from PIL import Image, ImageDraw
from uposatha.elements import MoonPhase

from compose import fifteen_day_appearance
from countdown import Countdown
from screen import WIDTH, HEIGHT, Ink


def test_draw_countdown(benchmark):
    image = Image.new(
        mode="P",
        size=(WIDTH, HEIGHT),
        color=Ink.WHITE.value
    )

    draw = ImageDraw.Draw(image)
    countdown = Countdown(fifteen_day_appearance(), date(2023, 7, 18), date(2023, 8, 1), MoonPhase.FULL)
    benchmark(countdown.draw, draw, 0, 0)
