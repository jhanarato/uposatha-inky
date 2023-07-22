import itertools
from dataclasses import dataclass
from collections.abc import Iterator

from PIL import Image, ImageFont, ImageDraw
from font_roboto import RobotoBold


class Font:
    def __init__(self, size: int):
        self._font = ImageFont.truetype(font=RobotoBold, size=size)

    @property
    def family(self) -> str:
        return self._font.font.family

    @property
    def style(self) -> str:
        return self._font.font.style

    def height(self, text: str) -> int:
        return self._font.getbbox(text)[3]

    def width(self, text: str) -> int:
        return self._font.getbbox(text)[2]

    def pil_font(self) -> ImageFont:
        return self._font

@dataclass
class BBox:
    left: int
    top: int
    right: int
    bottom: int

def font_bbox(text: str, font: ImageFont) -> BBox:
    bbox = font.getbbox(text)
    return BBox(*bbox)

def image_bbox(text: str, font: ImageFont) -> BBox:
    image = text_image(text, font)
    bbox = image.getbbox()
    return BBox(*bbox)

def pixel_bbox(text: str, font: ImageFont) -> BBox:
    image = text_image(text, font)
    pixels = black_pixels(image)
    return pixels_to_bbox(pixels)

def text_image(text, font):
    image = Image.new(mode="P", size=(100, 100), color=0)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, 1, font)
    return image

def black_pixels(image: Image) -> Iterator[tuple[int, int]]:
    pixels = image.load()
    columns = image.size[0]
    rows = image.size[1]

    for column, row in itertools.product(range(columns), range(rows)):
        if pixels[column, row] == 1:
            yield column, row

def pixels_to_bbox(pixels: Iterator[tuple[int, int]]) -> BBox:
    column, row = next(pixels)
    left = column
    right = column
    top = row
    bottom = row

    for column, row in pixels:
        left = min(left, column)
        right = max(right, column)
        top = min(top, row)
        bottom = min(bottom, row)

    return BBox(left=left, right=right, top=top, bottom=bottom)
