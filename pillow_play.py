# An experiment with Pillow.

from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

WIDTH = 400
HEIGHT = 300
BLACK = 1

img = Image.new(mode="RGB",
                size=(WIDTH, HEIGHT),
                color=(255, 255, 255))

draw = ImageDraw.Draw(img)
font = ImageFont.truetype(FredokaOne, 36)

message = "Hello, World!"
w, h = font.getsize(message)
x = (WIDTH / 2) - (w / 2)
y = (HEIGHT / 2) - (h / 2)

draw.text((x, y), message, (0, 0, 0), font)
img.show()
