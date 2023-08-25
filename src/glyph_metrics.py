from dataclasses import dataclass

from fontTools.ttLib import TTFont
from glyphtools import get_glyph_metrics

from design_units import DesignUnits


@dataclass
class GlyphMetrics:
    glyph_width: DesignUnits
    left_side_bearing: DesignUnits
    x_min: DesignUnits
    x_max: DesignUnits
    y_min: DesignUnits
    y_max: DesignUnits


def glyph_metrics(font_file_path: str, char: str):
    font = TTFont(font_file_path)
    upm = font['head'].unitsPerEm
    gt_metrics = get_glyph_metrics(font, char)
    return GlyphMetrics(
        glyph_width=DesignUnits(gt_metrics["fullwidth"], upm),
        left_side_bearing=DesignUnits(gt_metrics["lsb"], upm),
        x_min=DesignUnits(gt_metrics["xMin"], upm),
        x_max=DesignUnits(gt_metrics["xMax"], upm),
        y_min=DesignUnits(gt_metrics["yMin"], upm),
        y_max=DesignUnits(gt_metrics["yMax"], upm),
    )
