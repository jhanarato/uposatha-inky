import itertools
from dataclasses import dataclass
from collections.abc import Iterator

import glyphtools
from PIL import Image, ImageFont, ImageDraw
from fontTools.ttLib import TTFont
from font_roboto import RobotoBold


class DesignUnits:
    def __init__(self, units: int, units_per_em: int):
        self._units = units
        self._units_per_em = units_per_em

    def units(self) -> int:
        return self._units

    def to_em(self) -> float:
        return self.units() / self._units_per_em

    def to_points(self, font_size: int) -> float:
        return self.to_em() * font_size


@dataclass
class GlyphMetrics:
    glyph_width: DesignUnits
    left_side_bearing: DesignUnits


def extract_metrics(from_glyphtools: dict[str, int], units_per_em: int) -> GlyphMetrics:
    return GlyphMetrics(
        glyph_width=DesignUnits(from_glyphtools["width"], units_per_em),
        left_side_bearing=DesignUnits(from_glyphtools["lsb"], units_per_em),
    )


class Glyph:
    def __init__(self, font: TTFont, char: str):
        self._font = font
        self._char = char

    def _units_per_em(self) -> int:
        return self._font['head'].unitsPerEm

    def metrics(self) -> GlyphMetrics:
        gt_metrics = glyphtools.get_glyph_metrics(self._font, self._char)
        upm = self._units_per_em()
        return extract_metrics(gt_metrics, upm)


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


def glyph_centered_x(bbox: BBox, glyph_width: int, glyph_lsb: int) -> int:
    glyph_left = bbox.center[0] - (glyph_width // 2)
    return glyph_left - glyph_lsb


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
