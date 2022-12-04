# Script to display the uposatha on a Pimoroni Inky WHAT e-ink screen.

from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

what = InkyWHAT('yellow')
what.set_border(what.WHITE)

img = Image.new("P", (what.WIDTH, what.HEIGHT))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(FredokaOne, 36)

message = "Hello, World!"
w, h = font.getsize(message)
x = (what.WIDTH / 2) - (w / 2)
y = (what.HEIGHT / 2) - (h / 2)

draw.text((x, y), message, what.RED, font)
what.set_image(img)
what.show()
