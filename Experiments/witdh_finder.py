# Taken from this Stack Overflow question and refactored:
# https://stackoverflow.com/questions/4190667/how-to-get-width-of-a-truetype-font-character-in-1200ths-of-an-inch-with-python#61647653

from fontTools.ttLib import TTFont

def get_text_width(text: str, font: TTFont, point_size: int):
    character_map = font['cmap'].getcmap(3, 1).cmap
    glyph_set = font.getGlyphSet()
    widths = [code_point_width(ord(c), character_map, glyph_set) for c in text]
    return sum(widths) * size_factor(font, point_size)

def size_factor(font: TTFont, point_size: int) -> float:
    units_per_em = font['head'].unitsPerEm
    factor = point_size / units_per_em
    return factor

def code_point_width(code_point, character_map, glyph_set):
    if code_point in character_map and character_map[code_point] in glyph_set:
        point_width = glyph_set[character_map[code_point]].width
    else:
        point_width = glyph_set['.notdef'].width
    return point_width
