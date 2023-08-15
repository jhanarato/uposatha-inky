from PIL import ImageFont, Image

from font_roboto import RobotoBold

from bbox import BBox, image_bbox, font_bbox, black_pixels, pixels_to_bbox, pixel_bbox
from fonts import Font


def test_should_calculate_height_of_bbox():
    bbox = BBox(top=5, bottom=9, left=0, right=0)
    assert bbox.height == 5


def test_should_calculate_width_of_bbox():
    bbox = BBox(left=7, right=12, top=0, bottom=0)
    assert bbox.width == 6


def test_should_calculate_center_of_bbox():
    bbox = BBox(top=18, bottom=28, left=7, right=11)
    assert bbox.center == (9, 23)


def test_should_make_image_bbox():
    font = Font("roboto-bold", size=30)
    bbox = image_bbox("H", ImageFont.truetype(RobotoBold, 30))
    assert bbox.left == 2
    assert bbox.top == 7
    assert bbox.right == 18
    assert bbox.bottom == 27


def test_should_make_font_bbox():
    font = Font("roboto-bold", size=30)
    bbox = font_bbox("H", ImageFont.truetype(RobotoBold, 30))
    assert bbox.left == 0
    assert bbox.top == 7
    assert bbox.right == 21
    assert bbox.bottom == 28


def test_should_get_black_pixel_coordinates():
    image = Image.new(mode="P", size=(100, 100), color=0)
    pixels = image.load()
    pixels[13, 17] = 1
    pixels[55, 77] = 1
    assert list(black_pixels(image)) == [(13, 17), (55, 77)]


def test_should_convert_pixels_to_bounding_box():
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
