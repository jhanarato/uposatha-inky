# An experiment with Pillow.

from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

WIDTH = 400
HEIGHT = 300

img = Image.new(mode="RGB",
                size=(WIDTH, HEIGHT),
                color=(255, 255, 255))


def draw_centred_text(message):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FredokaOne, 36)
    w, h = font.getsize(message)
    x = (WIDTH / 2) - (w / 2)
    y = (HEIGHT / 2) - (h / 2)
    draw.text((x, y), message, (0, 0, 0), font)


def draw_multiline_text(message):
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype(FredokaOne, 36)
    draw.multiline_text(xy=(10, 10),
                        text=message,
                        font=fnt,
                        fill=(0, 0, 0))


draw_multiline_text("Hello\nWorld")
img.show()
