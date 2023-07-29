import pytest

from font_roboto import RobotoBold
from fontTools.ttLib import TTFont
from PIL import ImageFont

from fonts_x import Glyph, DesignUnits


@pytest.fixture
def glyph():
    font = TTFont(RobotoBold)
    return Glyph(font, "H")

def test_glyph_width_in_units(glyph):
    assert glyph.width().units() == 1448

def test_glyph_width_in_em(glyph):
    assert glyph.width().to_em() == 0.70703125

def test_glyph_width_in_points(glyph):
    assert glyph.width().to_points(font_size=16) == 11.3125

def test_glyph_left_side_bearing(glyph):
    assert glyph.left_side_bearing().units() == 130

def test_design_units_available():
    units = DesignUnits(units=100, units_per_em=2000)
    assert units.units() == 100

def test_design_units_converts_to_em():
    units = DesignUnits(units=100, units_per_em=2000)
    assert units.to_em() == 0.05

def test_design_converts_font_points_to_glyph_points():
    units = DesignUnits(units=100, units_per_em=2000)
    assert units.to_points(font_size=10) == 0.5
