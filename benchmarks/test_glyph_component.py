from PIL import Image, ImageDraw

from components import Glyph
from fonts import Font
from screen import Ink


def test_glyph_create(benchmark):
    benchmark(Glyph, "W", Font("roboto-bold", 30), Ink.BLACK)


def test_glyph_width(benchmark):
    glyph = Glyph("W", Font("roboto-bold", 30), Ink.BLACK)
    width = benchmark(glyph.width)
    assert width == 25


def test_glyph_height(benchmark):
    glyph = Glyph("W", Font("roboto-bold", 30), Ink.BLACK)
    height = benchmark(glyph.width)
    assert height == 25


def test_relative_x(benchmark):
    glyph = Glyph("W", Font("roboto-bold", 30), Ink.BLACK)
    x = benchmark(glyph.relative_x, 10)
    assert x == 9


def test_relative_y(benchmark):
    glyph = Glyph("W", Font("roboto-bold", 30), Ink.BLACK)
    y = benchmark(glyph.relative_y, 11)
    assert y == 4


def test_glyph_draw(benchmark):
    image = Image.new(
        mode="P",
        size=(100, 100),
        color=Ink.WHITE.value
    )

    draw = ImageDraw.Draw(image)

    glyph = Glyph("W", Font("roboto-bold", 30), Ink.BLACK)
    benchmark(glyph.draw, draw, 0, 0)
