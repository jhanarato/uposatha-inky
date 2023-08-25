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
