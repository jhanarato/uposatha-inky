from PIL import Image, ImageDraw, ImageFont
from font_fredoka_one import FredokaOne

from content import NextUposathaContent

def make_image(content: NextUposathaContent) -> Image:
    image = Image.new(mode="P", size=(400, 300))

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(FredokaOne, 36)

    w, h = font.getsize(content.date)
    x = (400 / 2) - (w / 2)
    y = (300 / 2) - (h / 2)

    draw.text((x, y), content.date, 1, font)

    return image
