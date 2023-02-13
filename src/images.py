from PIL import Image, ImageDraw, ImageFont
from font_fredoka_one import FredokaOne

def make_image(text: str) -> Image:
    image = Image.new(mode="P", size=(400, 300))

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(FredokaOne, 36)

    w, h = font.getsize(text)
    x = (400 / 2) - (w / 2)
    y = (300 / 2) - (h / 2)

    draw.text((x, y), text, 1, font)

    return image
