import pytest
from font_roboto import RobotoBold

from components import Glyph
from bbox import image_bbox
from fonts import DesignUnits


def test_should_give_width_in_pixels():
    glyph = Glyph(font_size=30, char="H")
    pixels = round(DesignUnits(1448, 2048).to_points(30))
    assert glyph.width() == pixels


def test_should_give_height_in_pixels():
    glyph = Glyph(font_size=30, char="H")
    assert glyph.height() == 21
