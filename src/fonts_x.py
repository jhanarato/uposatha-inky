""" Experimental fonts module. """

from fontTools.ttLib import TTFont

def text_width_in_points(text: str, font: TTFont, font_points_per_em: int) -> float:
    return sum([glyph_width_in_points(ord(c), font, font_points_per_em) for c in text])

def glyph_width_in_points(code: int, font: TTFont, font_points_per_em: int) -> float:
    glyph = Glyph(font, font_points_per_em, code)
    return glyph.width_in_points

def glyph_width_in_em(code: int, font: TTFont) -> float:
    return glyph_width_in_units(code, font) / units_per_em(font)

def glyph_width_in_units(code: int, font: TTFont) -> int:
    return glyph(code, font).width

def units_per_em(font: TTFont) -> int:
    return font['head'].unitsPerEm

def glyph(code: int, font: TTFont):
    character_map = font['cmap'].getcmap(3, 1).cmap
    glyph_set = font.getGlyphSet()

    if code not in character_map:
        raise RuntimeError(f"Code {code} not in character map")

    character = character_map[code]

    if character not in glyph_set:
        raise RuntimeError(f"Character {character} not in glyph set.")

    return glyph_set[character]

class Glyph:
    def __init__(self, font: TTFont, points: int, code: int):
        self._font = font
        self._points = points
        self._glyph = glyph(code, font)

    @property
    def width_in_units(self) -> int:
        return self._glyph.width

    @property
    def width_in_em(self) -> float:
        return self.width_in_units / self.units_per_em

    @property
    def width_in_points(self) -> float:
        return self.width_in_em * self._points

    @property
    def units_per_em(self) -> int:
        return self._font['head'].unitsPerEm
