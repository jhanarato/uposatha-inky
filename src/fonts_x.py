""" Experimental fonts module. """

from fontTools.ttLib import TTFont

def text_width_in_points(text: str, font: TTFont, font_points: int) -> float:
    design_units = [glyph(ord(c), font).width for c in text]
    return sum(design_units) * scale_factor(font, font_points)

def glyph(code: int, font: TTFont):
    character_map = font['cmap'].getcmap(3, 1).cmap
    glyph_set = font.getGlyphSet()

    if code not in character_map:
        raise RuntimeError(f"Code {code} not in character map")

    character = character_map[code]

    if character not in glyph_set:
        raise RuntimeError(f"Character {character} not in glyph set.")

    return glyph_set[character]

def scale_factor(font: TTFont, font_points: int) -> float:
    upm = font['head'].unitsPerEm
    return font_points / upm
