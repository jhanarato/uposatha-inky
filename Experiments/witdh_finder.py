# Taken from this Stack Overflow question and refactored:
# https://stackoverflow.com/questions/4190667/how-to-get-width-of-a-truetype-font-character-in-1200ths-of-an-inch-with-python#61647653

from fontTools.ttLib import TTFont

def get_text_width(text: str, font: TTFont, point_size: int):
    character_map = font['cmap'].getcmap(3, 1).cmap
    glyph_set = font.getGlyphSet()
    widths = [code_point_width(ord(c), character_map, glyph_set) for c in text]
    total_width = sum(widths)
    return width_in_pixels(total_width, font, point_size)

def width_in_pixels(width: int, font: TTFont, point_size: int) -> float:
    units_per_em = font['head'].unitsPerEm
    return width * point_size / units_per_em

def code_point_width(code_point, character_map, glyph_set):
    if code_point not in character_map:
        raise RuntimeError("Code point not in character map")

    if character_map[code_point] not in glyph_set:
        raise RuntimeError("Character not in glyph set")

    return glyph_set[character_map[code_point]].width
