from typing import Protocol

import font_roboto
from PIL import ImageFont

from design_units import DesignUnits
from font_metrics import GlyphMetrics

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


class Metrics(Protocol):
    def units_per_em(self, file_path: str) -> int: ...
    def glyph_metrics(self, file_path: str, char: str) -> GlyphMetrics: ...


class Font:
    def __init__(self, name: str, size: int):
        self._name = name
        self._size = size
        self._pil_font = ImageFont.truetype(self.path, size=size)

    @property
    def path(self) -> str:
        return fonts[self._name]

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
