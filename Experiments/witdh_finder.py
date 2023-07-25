# Taken from this Stack Overflow question and refactored:
# https://stackoverflow.com/questions/4190667/how-to-get-width-of-a-truetype-font-character-in-1200ths-of-an-inch-with-python#61647653

from fontTools.ttLib import TTFont

def get_text_width(text: str, font: TTFont, point_size: int):
    character_map = font['cmap'].getcmap(3, 1).cmap
    glyph_set = font.getGlyphSet()
    units_per_em = font['head'].unitsPerEm

    total = 0
    for c in text:
        code_point = ord(c)
        if code_point in character_map and character_map[code_point] in glyph_set:
            total += glyph_set[character_map[code_point]].width
        else:
            total += glyph_set['.notdef'].width
    total = total * float(point_size) / units_per_em
    return total
