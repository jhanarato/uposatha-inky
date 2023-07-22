import pytest

from PIL import ImageFont
from font_roboto import RobotoBold

from fonts import Font, image_bbox, BBox, font_bbox


@pytest.fixture
def font():
    return Font(size=30)

def test_should_have_family(font):
    assert font.family == "Roboto"

def test_should_have_style(font):
    assert font.style == "Bold"

def test_should_measure_height_of_text(font):
    assert font.height("Hello") == 28

def test_should_measure_width_of_text(font):
    assert font.width("Hello") == 70

def test_should_make_image_bbox(font):
    bbox = image_bbox("H", ImageFont.truetype(RobotoBold, 30))
    assert bbox.left == 2
    assert bbox.top == 7
    assert bbox.right == 19
    assert bbox.bottom == 28

def test_should_make_font_bbox(font):
    bbox = font_bbox("H", ImageFont.truetype(RobotoBold, 30))
    assert bbox.left == 0
    assert bbox.top == 7
    assert bbox.right == 21
    assert bbox.bottom == 28

