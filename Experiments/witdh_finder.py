# Taken from this Stack Overflow question and refactored:
# https://stackoverflow.com/questions/4190667/how-to-get-width-of-a-truetype-font-character-in-1200ths-of-an-inch-with-python#61647653

from fontTools.ttLib import TTFont

def get_text_width(text: str, font: TTFont, points: int):
    widths = [code_point_width(ord(c), font) for c in text]
    total_width = sum(widths)
    return width_in_pixels(total_width, font, points)

def width_in_pixels(width: int, font: TTFont, points: int) -> float:
    units_per_em = font['head'].unitsPerEm
    return width * points / units_per_em

def glyph(code_point: int, font: TTFont):
    character_map = font['cmap'].getcmap(3, 1).cmap
    glyph_set = font.getGlyphSet()

    if code_point not in character_map:
        return None
    if character_map[code_point] not in glyph_set:
        return None

    return glyph_set[character_map[code_point]]

def code_point_width(code_point, font):
    return glyph(code_point, font).width
