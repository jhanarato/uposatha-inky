from PIL import Image, ImageDraw

from components import DayOfWeekIcon
from compose import SMALLEST_ICON


def display(icon: DayOfWeekIcon):
    border = 10
    image = Image.new(mode="P", size=(icon.width() + border * 2, icon.height() + border * 2), color=0)
    draw = ImageDraw.Draw(image)

    icon.draw(draw, border, border)

    palette = [
        255, 255, 255,  # 0 = WHITE
        0, 0, 0,  # 1 = BLACK
        255, 255, 0  # 2 = YELLOW
    ]
    image.putpalette(palette)
    converted = image.convert(mode="RGB")
    converted.show()

display(DayOfWeekIcon("S", SMALLEST_ICON))
