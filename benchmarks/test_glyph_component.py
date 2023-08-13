from PIL import Image, ImageDraw

from components import Glyph
from screen import Ink


def test_glyph_create(benchmark):
    benchmark(Glyph, "W", 30, Ink.BLACK)


def test_glyph_width(benchmark):
    glyph = Glyph("W", 30, Ink.BLACK)
    width = benchmark(glyph.width)
    assert width == 26


def test_glyph_height(benchmark):
    glyph = Glyph("W", 30, Ink.BLACK)
    height = benchmark(glyph.width)
    assert height == 26


def test_glyph_draw(benchmark):
    image = Image.new(
        mode="P",
        size=(100, 100),
        color=Ink.WHITE.value
    )

    draw = ImageDraw.Draw(image)

    glyph = Glyph("W", 30, Ink.BLACK)
    benchmark(glyph.draw, draw, 0, 0)
