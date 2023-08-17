from dataclasses import dataclass

import glyphtools
from PIL import ImageFont
from fontTools.ttLib import TTFont
import font_roboto


fonts = {
    "roboto": font_roboto.Roboto,
    "roboto-black": font_roboto.RobotoBlack,
    "roboto-black-italic": font_roboto.RobotoBlackItalic,
    "roboto-bold": font_roboto.RobotoBold,
    "roboto-bold-italic": font_roboto.RobotoItalic,
    "roboto-italic": font_roboto.RobotoItalic,
    "roboto-light": font_roboto.RobotoLight,
    "roboto-light-italic": font_roboto.RobotoLightItalic,
    "roboto-medium": font_roboto.RobotoMedium,
    "roboto-medium-italic": font_roboto.RobotoMediumItalic,
    "roboto-thin": font_roboto.RobotoThin,
    "roboto-thin-italic": font_roboto.RobotoThinItalic,
}


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
    x_min: DesignUnits
    x_max: DesignUnits
    y_min: DesignUnits
    y_max: DesignUnits


class Font:
    def __init__(self, name: str, size: int):
        self._pil_font = ImageFont.truetype(font=fonts[name], size=size)
        self._ft_font = TTFont(fonts[name])
        self._size = size

    @property
    def family(self) -> str:
        return self._pil_font.font.family

    @property
    def style(self) -> str:
        return self._pil_font.font.style

    @property
    def size(self) -> int:
        return self._size

    def ascent(self) -> int:
        return self._pil_font.getmetrics()[0]

    def descent(self) -> int:
        return self._pil_font.getmetrics()[1]

    def height(self, text: str) -> int:
        return self._pil_font.getbbox(text)[3]

    def width(self, text: str) -> int:
        return self._pil_font.getbbox(text)[2]

    def as_pillow(self) -> ImageFont:
        return self._pil_font

    def glyph_metrics(self, char: str) -> GlyphMetrics:
        gt_metrics = glyphtools.get_glyph_metrics(self._ft_font, char)
        return GlyphMetrics(
            glyph_width=DesignUnits(gt_metrics["fullwidth"], self.upm()),
            left_side_bearing=DesignUnits(gt_metrics["lsb"], self.upm()),
            x_min=DesignUnits(gt_metrics["xMin"], self.upm()),
            x_max=DesignUnits(gt_metrics["xMax"], self.upm()),
            y_min=DesignUnits(gt_metrics["yMin"], self.upm()),
            y_max=DesignUnits(gt_metrics["yMax"], self.upm()),
        )

    def upm(self):
        return self._ft_font['head'].unitsPerEm
