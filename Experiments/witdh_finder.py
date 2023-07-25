# Taken from this Stack Overflow question and refactored:
# https://stackoverflow.com/questions/4190667/how-to-get-width-of-a-truetype-font-character-in-1200ths-of-an-inch-with-python#61647653

from fontTools.ttLib import TTFont

def get_text_width(text: str, font: TTFont, point_size: int):
    units_per_em = font['head'].unitsPerEm
    character_map = font['cmap'].getcmap(3, 1).cmap
    glyph_set = font.getGlyphSet()

    total = 0

    for c in text:
        code_point = ord(c)
        point_width = code_point_width(code_point, character_map, glyph_set)
        total += point_width
    total = total * (point_size / units_per_em)
    return total

def code_point_width(code_point, character_map, glyph_set):
    if code_point in character_map and character_map[code_point] in glyph_set:
        point_width = glyph_set[character_map[code_point]].width
    else:
        point_width = glyph_set['.notdef'].width
    return point_width
