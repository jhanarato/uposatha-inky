from components import Glyph
from fonts import Font
from screen import Ink


def test_should_give_width_in_pixels():
    glyph = Glyph("W", Font("roboto-bold", 30), Ink.BLACK)
    assert glyph.width() == 25


def test_should_give_height_in_pixels():
    glyph = Glyph("W", Font("roboto-bold", 30), Ink.BLACK)
    assert glyph.height() == 21


def test_should_calculate_left_bearing():
    glyph = Glyph("W", Font("roboto-bold", 30), Ink.BLACK)
    assert glyph._left_bearing().to_pixels() == 1


def test_should_calculate_top_bearing():
    glyph = Glyph("W", Font("roboto-bold", 30), Ink.BLACK)
    assert glyph._top_bearing().to_pixels() == 7
