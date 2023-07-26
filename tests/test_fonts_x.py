import pytest

from font_roboto import RobotoBold
from fontTools.ttLib import TTFont
from PIL import ImageFont

from fonts_x import text_width_in_points, Glyph


# Approval test for refactoring. I just switched the
# font in the original script, the value is what was returned
# before I changed anything else.
def test_text_width_in_points():
    text = 'This is a test'
    font = TTFont(RobotoBold)
    assert text_width_in_points(text, font, 12) == 69.029296875

def test_pillow_sets_point_equal_to_pixel():
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
    points = 16
    return Glyph(font, points, code)

def test_upm(glyph):
    assert glyph.units_per_em == 2048

def test_glyph_width_in_units(glyph):
    assert glyph.width_in_units == 1448

def test_glyph_width_in_em(glyph):
    assert glyph.width_in_em == 0.70703125

def test_glyph_width_in_points(glyph):
    assert glyph.width_in_points == 11.3125
