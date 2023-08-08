from dataclasses import dataclass

import glyphtools
from PIL import ImageFont
from fontTools.ttLib import TTFont
from font_roboto import RobotoBold

from bbox import BBox


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

    def metrics(self) -> GlyphMetrics:
        gt_metrics = glyphtools.get_glyph_metrics(self._font, self._char)
        upm = self._font['head'].unitsPerEm
        return extract_metrics(gt_metrics, upm)


class Font:
    def __init__(self, size: int):
        self._pil_font = ImageFont.truetype(font=RobotoBold, size=size)
        self._ft_font = TTFont(RobotoBold)

    @property
    def family(self) -> str:
        return self._pil_font.font.family

    @property
    def style(self) -> str:
        return self._pil_font.font.style

    def height(self, text: str) -> int:
        return self._pil_font.getbbox(text)[3]

    def width(self, text: str) -> int:
        return self._pil_font.getbbox(text)[2]

    def pil_font(self) -> ImageFont:
        return self._pil_font

    def fonttools_font(self) -> TTFont:
        return self._ft_font

    def glyph_metrics(self, char: str) -> GlyphMetrics:
        glyph = Glyph(self._ft_font, char)
        return glyph.metrics()


def glyph_centered_x(bbox: BBox, metrics: GlyphMetrics, font_points: int) -> int:
    width = metrics.glyph_width.to_points(font_points)
    lsb = metrics.left_side_bearing.to_points(font_points)

    glyph_left = bbox.center[0] - (width // 2)

    return round(glyph_left - lsb)
