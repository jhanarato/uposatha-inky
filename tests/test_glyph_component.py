from components import Glyph
from screen import Ink


def test_should_give_width_in_pixels():
    glyph = Glyph("W", 30, Ink.BLACK)
    assert glyph.width() == 26


def test_should_give_height_in_pixels():
    glyph = Glyph("W", 30, Ink.BLACK)
    assert glyph.height() == 21


def test_should_find_relative_x():
    glyph = Glyph("W", 30, Ink.BLACK)
    assert glyph.relative_x(10) == 9


def test_should_find_relative_y():
    glyph = Glyph("W", 30, Ink.BLACK)
    assert glyph.relative_y(11) == 4
