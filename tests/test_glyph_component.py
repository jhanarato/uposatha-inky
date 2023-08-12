import pytest
from font_roboto import RobotoBold

from components import Glyph
from bbox import image_bbox
from fonts import DesignUnits


def test_should_give_width_in_pixels():
    glyph = Glyph("W", 30)
    assert glyph.width() == 26


def test_should_give_height_in_pixels():
    glyph = Glyph(char="W", font_size=30)
    assert glyph.height() == 21
