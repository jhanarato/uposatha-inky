""" Experimental fonts module. """

from fontTools.ttLib import TTFont
import glyphtools

def text_width_in_points(text: str, font: TTFont, font_points_per_em: int) -> float:
    glyphs = [Glyph(font, ord(c)) for c in text]
    return sum([glyph.width_in_points(font_points_per_em) for glyph in glyphs])

class Glyph:
    def __init__(self, font: TTFont, code: int):
        self._font = font
        self._units_per_em = self._font['head'].unitsPerEm
        self._glyph = self._get_glyph(code, font)

    def _get_glyph(self, code: int, font: TTFont):
        character_map = font['cmap'].getcmap(3, 1).cmap
        glyph_set = font.getGlyphSet()

        if code not in character_map:
            raise RuntimeError(f"Code {code} not in character map")

        character = character_map[code]

        if character not in glyph_set:
            raise RuntimeError(f"Character {character} not in glyph set.")

        return glyph_set[character]

    def width_in_units(self) -> int:
        return self._glyph.width

    def width_in_em(self) -> float:
        return self.width_in_units() / self._units_per_em

    def width_in_points(self, font_points: int) -> float:
        return self.width_in_em() * font_points

    def left_side_bearing(self) -> int:
        return self._glyph.lsb


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
