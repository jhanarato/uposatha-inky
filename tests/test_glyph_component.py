from components import Glyph


def test_should_give_width_in_pixels():
    glyph = Glyph("W", 30)
    assert glyph.width() == 26


def test_should_give_height_in_pixels():
    glyph = Glyph("W", 30)
    assert glyph.height() == 21


def test_should_find_relative_x():
    glyph = Glyph("W", 30)
    assert glyph.relative_x(10) == 9
