import itertools
from dataclasses import dataclass
from typing import Iterator

from PIL import ImageFont, Image, ImageDraw


@dataclass
class BBox:
    left: int
    top: int
    right: int
    bottom: int

    @property
    def height(self) -> int:
        return self.bottom - self.top + 1

    @property
    def width(self) -> int:
        return self.right - self.left + 1

    @property
    def center(self) -> tuple[int, int]:
        x = self.left + self.width // 2
        y = self.top + self.height // 2
        return x, y

    def __str__(self):
        out = f"Top: {self.top}"
        out += f" Bottom: {self.bottom}"
        out += f" Left: {self.left}"
        out += f" Right: {self.right}"
        return out


def font_bbox(text: str, font: ImageFont) -> BBox:
    bbox = font.getbbox(text)
    return BBox(*bbox)


def image_bbox(text: str, font: ImageFont) -> BBox:
    image = text_image(text, font)
    bbox = image.getbbox()
    return BBox(bbox[0], bbox[1], bbox[2] - 1, bbox[3] - 1)


def pixel_bbox(text: str, font: ImageFont) -> BBox:
    image = text_image(text, font)
    pixels = black_pixels(image)
    return pixels_to_bbox(pixels)


def text_image(text: str, font: ImageFont):
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
        bottom = max(bottom, row)

    return BBox(left=left, right=right, top=top, bottom=bottom)
