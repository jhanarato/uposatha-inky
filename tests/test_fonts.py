import pytest

from PIL import Image, ImageFont
from fontTools.ttLib import TTFont
from font_roboto import RobotoBold

from fonts import Font, image_bbox, font_bbox, black_pixels, pixels_to_bbox, pixel_bbox, BBox, glyph_centered_x, \
    extract_metrics
from fonts import DesignUnits, Glyph


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


def test_should_calculate_height_of_bbox():
    bbox = BBox(top=5, bottom=9, left=0, right=0)
    assert bbox.height == 5


def test_should_calculate_width_of_bbox():
    bbox = BBox(left=7, right=12, top=0, bottom=0)
    assert bbox.width == 6


def test_should_calculate_center_of_bbox():
    bbox = BBox(top=18, bottom=28, left=7, right=11)
    assert bbox.center == (9, 23)


def test_should_make_image_bbox(font):
    bbox = image_bbox("H", ImageFont.truetype(RobotoBold, 30))
    assert bbox.left == 2
    assert bbox.top == 7
    assert bbox.right == 18
    assert bbox.bottom == 27


def test_should_make_font_bbox(font):
    bbox = font_bbox("H", ImageFont.truetype(RobotoBold, 30))
    assert bbox.left == 0
    assert bbox.top == 7
    assert bbox.right == 21
    assert bbox.bottom == 28


def test_should_get_black_pixel_coordinates(font):
    image = Image.new(mode="P", size=(100, 100), color=0)
    pixels = image.load()
    pixels[13, 17] = 1
    pixels[55, 77] = 1
    assert list(black_pixels(image)) == [(13, 17), (55, 77)]


def test_should_convert_pixels_to_bounding_box(font):
    image = Image.new(mode="P", size=(100, 100), color=0)
    pixels = image.load()
    pixels[13, 17] = 1
    pixels[55, 77] = 1
    bbox = pixels_to_bbox(black_pixels(image))
    assert bbox.left == 13
    assert bbox.top == 17
    assert bbox.right == 55
    assert bbox.bottom == 77


def test_should_adjust_image_bbox_to_match_pixel_bbox():
    text = "Hello"
    font = ImageFont.truetype(RobotoBold, 30)
    image = image_bbox(text, font)
    pixel = pixel_bbox(text, font)
    assert pixel.left == image.left
    assert pixel.top == image.top
    assert pixel.right == image.right
    assert pixel.bottom == image.bottom


def test_should_align_text_baseline_when_no_descent():
    text = "Hello"
    font = ImageFont.truetype(RobotoBold, 30)
    bottoms = [pixel_bbox(c, font).bottom for c in text]
    assert len(set(bottoms)) == 1


def test_should_be_below_baseline_when_descent():
    font = ImageFont.truetype(RobotoBold, 30)
    above = pixel_bbox("H", font).bottom
    below = pixel_bbox("y", font).bottom
    assert below > above


@pytest.fixture
def glyph():
    font = TTFont(RobotoBold)
    return Glyph(font, "H")


def test_glyph_width_in_units(glyph):
    assert glyph.metrics().glyph_width.units() == 1448


def test_glyph_width_in_em(glyph):
    assert glyph.metrics().glyph_width.to_em() == 0.70703125


def test_glyph_width_in_points(glyph):
    assert glyph.metrics().glyph_width.to_points(font_size=16) == 11.3125


def test_glyph_left_side_bearing(glyph):
    assert glyph.metrics().left_side_bearing.units() == 130


def test_design_units_available():
    units = DesignUnits(units=100, units_per_em=2000)
    assert units.units() == 100


def test_design_units_converts_to_em():
    units = DesignUnits(units=100, units_per_em=2000)
    assert units.to_em() == 0.05


def test_design_converts_font_points_to_glyph_points():
    units = DesignUnits(units=100, units_per_em=2000)
    assert units.to_points(font_size=10) == 0.5


def test_glyph_with_space():
    with pytest.raises(KeyError):
        glyph = Glyph(TTFont(RobotoBold), " ")


def test_lsb_as_points(glyph):
    assert glyph.metrics().left_side_bearing.to_points(font_size=30) == 1.904296875


def test_should_center_glyph_horizontally():
    bbox = BBox(left=10, right=60, top=20, bottom=40)
    assert bbox.center[0] == 35
    glyph_width_in_pixels = 10
    glyph_lsb_in_pixels = 5
    assert glyph_centered_x(bbox, glyph_width_in_pixels, glyph_lsb_in_pixels) == 25


def test_should_convert_glyph_metrics():
    glyphtools_dict = {"width": 100, "lsb": 200}
    metrics = extract_metrics(glyphtools_dict, 0)
    assert metrics.glyph_width.units() == 100
