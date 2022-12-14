# Script to display the uposatha on a Pimoroni Inky WHAT e-ink screen.

from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
import icalendar
from forest_sangha_moons.MahanikayaCalendar import MahanikayaCalendar

with open("mahanikaya.ical", "r") as f:
    content = f.read()

ical = icalendar.Calendar.from_ical(content)
calendar = MahanikayaCalendar()
calendar.import_ical(ical)
next_uposatha = calendar.next_uposatha()
uposatha_date = next_uposatha.date.strftime("%A, %d %b %y")

what = InkyWHAT('yellow')
what.set_border(what.WHITE)

img = Image.new("P", (what.WIDTH, what.HEIGHT))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(FredokaOne, 36)

w, h = font.getsize(uposatha_date)
x = (what.WIDTH / 2) - (w / 2)
y = (what.HEIGHT / 2) - (h / 2)

draw.text((x, y), uposatha_date, what.BLACK, font)
what.set_image(img)
what.show()
