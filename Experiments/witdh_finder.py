# Taken from this Stack Overflow question and refactored:
# https://stackoverflow.com/questions/4190667/how-to-get-width-of-a-truetype-font-character-in-1200ths-of-an-inch-with-python#61647653

from fontTools.ttLib import TTFont

def get_text_width(text: str, font: TTFont, points: int):
    widths = [glyph(ord(c), font).width for c in text]
    total_width = sum(widths)
    return total_width * scale_factor(font, points)

def glyph(code: int, font: TTFont):
    character_map = font['cmap'].getcmap(3, 1).cmap
    glyph_set = font.getGlyphSet()

    if code not in character_map:
        return None
    if character_map[code] not in glyph_set:
        return None

    return glyph_set[character_map[code]]

def scale_factor(font, points):
    return points / font['head'].unitsPerEm

