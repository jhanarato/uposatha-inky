from dataclasses import dataclass

import font_roboto
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


class MetricsPrecalculated:
    def __init__(self):
        self._metrics = {
            font_roboto.RobotoBold: {
                "S": GlyphMetrics(
                    x_min=DesignUnits(70, 2048),
                    x_max=DesignUnits(1187, 2048),
                    y_min=DesignUnits(-20, 2048),
                    y_max=DesignUnits(1476, 2048)
                ),
                "M": GlyphMetrics(
                    x_min=DesignUnits(130, 2048),
                    x_max=DesignUnits(1662, 2048),
                    y_min=DesignUnits(0, 2048),
                    y_max=DesignUnits(1456, 2048)
                ),
                "T": GlyphMetrics(
                    x_min=DesignUnits(41, 2048),
                    x_max=DesignUnits(1226, 2048),
                    y_min=DesignUnits(0, 2048),
                    y_max=DesignUnits(1456, 2048)
                ),
                "W": GlyphMetrics(
                    x_min=DesignUnits(35, 2048),
                    x_max=DesignUnits(1759, 2048),
                    y_min=DesignUnits(0, 2048),
                    y_max=DesignUnits(1456, 2048)
                ),
                "F": GlyphMetrics(
                    x_min=DesignUnits(130, 2048),
                    x_max=DesignUnits(1079, 2048),
                    y_min=DesignUnits(0, 2048),
                    y_max=DesignUnits(1456, 2048)
                ),
            },
        }

    def units_per_em(self, file_path: str) -> int:
        return 2048

    def glyph_metrics(self, file_path: str, char: str) -> GlyphMetrics:
        return self._metrics[file_path][char]
