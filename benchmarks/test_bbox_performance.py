from PIL import ImageFont
from font_roboto import RobotoBold

from bbox import font_bbox, image_bbox, pixel_bbox


def test_font_bbox(benchmark):
    benchmark(font_bbox, 'H', ImageFont.truetype(RobotoBold, 30))


def test_image_bbox(benchmark):
    benchmark(image_bbox, 'H', ImageFont.truetype(RobotoBold, 30))


def test_pixel_bbox(benchmark):
    benchmark(pixel_bbox, 'H', ImageFont.truetype(RobotoBold, 30))
