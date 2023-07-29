import pytest

from font_roboto import RobotoBold
from fontTools.ttLib import TTFont
from PIL import ImageFont

from fonts_x import text_width_in_points, Glyph, DesignUnits


def test_approval():
    """ Test that the code still does as it did when I started refactoring """
    text = 'This is a test'
    font = TTFont(RobotoBold)
    assert text_width_in_points(text, font, 12) == 69.029296875

def test_pillow_pixels_equal_points():
    """
    Pillow pixels per em (PPM) is the same as points per em
    i.e. One pixel equals one point when drawing text.
    """
    size = 30
    text = "H"

    ft_font = TTFont(RobotoBold)
    pil_font = ImageFont.truetype(RobotoBold, size)

    ft_width = text_width_in_points(text, ft_font, size)
    pil_width = pil_font.getlength(text)

    assert ft_width == pytest.approx(pil_width, 0.001)

@pytest.fixture
def glyph():
    font = TTFont(RobotoBold)
    code = ord("H")
    return Glyph(font, code)

def test_glyph_width_in_units(glyph):
    assert glyph.width_in_units() == 1448

def test_glyph_width_in_em(glyph):
    assert glyph.width_in_em() == 0.70703125

def test_glyph_width_in_points(glyph):
    assert glyph.width_in_points(16) == 11.3125

def test_glyph_left_side_bearing(glyph):
    # I assume the result is in units. That is to be confirmed.
    assert glyph.left_side_bearing() == 130

def test_design_units_available():
    units = DesignUnits(units=100, units_per_em=2000)
    assert units.units() == 100

def test_design_units_converts_to_em():
    units = DesignUnits(units=100, units_per_em=2000)
    assert units.to_em() == 0.05
