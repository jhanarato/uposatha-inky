from dataclasses import dataclass

from fontTools.ttLib import TTFont
from glyphtools import get_glyph_metrics

from design_units import DesignUnits


@dataclass
class GlyphMetrics:
    x_min: DesignUnits
    x_max: DesignUnits
    y_min: DesignUnits
    y_max: DesignUnits

    @property
    def width(self) -> DesignUnits:
        return self.x_max - self.x_min

    @property
    def height(self) -> DesignUnits:
        return self.y_max - self.y_min


def glyph_metrics(font_file_path: str, char: str):
    font = TTFont(font_file_path)
    upm = font['head'].unitsPerEm
    gt_metrics = get_glyph_metrics(font, char)
    return GlyphMetrics(
        x_min=DesignUnits(gt_metrics["xMin"], upm),
        x_max=DesignUnits(gt_metrics["xMax"], upm),
        y_min=DesignUnits(gt_metrics["yMin"], upm),
        y_max=DesignUnits(gt_metrics["yMax"], upm),
    )


class MetricsFromFile:
    def units_per_em(self, file_path: str) -> int:
        font = TTFont(file_path)
        return font['head'].unitsPerEm

    def glyph_metrics(self, file_path: str, char: str) -> GlyphMetrics:
        font = TTFont(file_path)
        upm = font['head'].unitsPerEm
        gt_metrics = get_glyph_metrics(font, char)
        return GlyphMetrics(
            x_min=DesignUnits(gt_metrics["xMin"], upm),
            x_max=DesignUnits(gt_metrics["xMax"], upm),
            y_min=DesignUnits(gt_metrics["yMin"], upm),
            y_max=DesignUnits(gt_metrics["yMax"], upm),
        )
