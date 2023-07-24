from PIL import Image, ImageFont, ImageDraw
from font_roboto import RobotoBold

palette = [
    255, 255, 255,  # 0 = WHITE
    0, 0, 0,        # 1 = BLACK
    255, 255, 0     # 2 = YELLOW
]

font = ImageFont.truetype(RobotoBold, 50)
text = "S"
bbox = font.getbbox(text)
image = Image.new(mode="P", size=(50, 50), color=0)
draw = ImageDraw.Draw(image)
draw.rectangle(bbox, fill=1)
draw.text((0, 0), text, 0, font)
image.putpalette(palette)
converted = image.convert(mode="RGB")
converted.show()
