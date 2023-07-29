""" Experimental fonts module. """

from fontTools.ttLib import TTFont
import glyphtools


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


class Glyph:
    def __init__(self, font: TTFont, char: str):
        self._font = font
        self._char = char
        self._glyph = get_glyph(ord(char), font)
        self._metrics = glyphtools.get_glyph_metrics(font, char)

    def _units_per_em(self) -> int:
        return self._font['head'].unitsPerEm

    def width(self) -> DesignUnits:
        return DesignUnits(self._metrics["width"], self._units_per_em())

    def left_side_bearing(self) -> DesignUnits:
        return DesignUnits(self._metrics["lsb"], self._units_per_em())


def get_glyph(code: int, font: TTFont):
    character_map = font['cmap'].getcmap(3, 1).cmap
    glyph_set = font.getGlyphSet()

    if code not in character_map:
        raise RuntimeError(f"Code {code} not in character map")

    character = character_map[code]

    if character not in glyph_set:
        raise RuntimeError(f"Character {character} not in glyph set.")

    return glyph_set[character]
