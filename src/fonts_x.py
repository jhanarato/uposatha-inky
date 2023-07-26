""" Experimental fonts module. """

from fontTools.ttLib import TTFont

def text_width_in_points(text: str, font: TTFont, font_points_per_em: int) -> float:
    return sum([glyph_width_in_points(ord(c), font, font_points_per_em) for c in text])

def glyph_width_in_points(code: int, font: TTFont, font_points_per_em: int) -> float:
    return font_points_per_em * glyph(code, font).width / units_per_em(font)

def glyph(code: int, font: TTFont):
    character_map = font['cmap'].getcmap(3, 1).cmap
    glyph_set = font.getGlyphSet()

    if code not in character_map:
        raise RuntimeError(f"Code {code} not in character map")

    character = character_map[code]

    if character not in glyph_set:
        raise RuntimeError(f"Character {character} not in glyph set.")

    return glyph_set[character]

def units_per_em(font: TTFont) -> int:
    return font['head'].unitsPerEm
