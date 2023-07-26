""" Experimental fonts module. """

from fontTools.ttLib import TTFont

def text_width(text: str, font: TTFont, points: int) -> float:
    widths = [glyph(ord(c), font).width for c in text]
    return sum(widths) * scale_factor(font, points)

def glyph(code: int, font: TTFont):
    character_map = font['cmap'].getcmap(3, 1).cmap
    glyph_set = font.getGlyphSet()

    if code not in character_map:
        return None
    if character_map[code] not in glyph_set:
        return None

    return glyph_set[character_map[code]]

def scale_factor(font: TTFont, points: int) -> float:
    return points / font['head'].unitsPerEm