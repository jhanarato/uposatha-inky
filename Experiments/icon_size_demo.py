from PIL import Image, ImageDraw

from components import DayOfWeekIcon
from compose import SMALLEST_ICON, SMALL_ICON, MEDIUM_ICON, LARGE_ICON, LARGEST_ICON, GAP


def days(size: int) -> list[DayOfWeekIcon]:
    return [DayOfWeekIcon(letter, size) for letter in "SMTWF"]

def draw_icons(draw: ImageDraw):
    letters = "SMTWF"
    sizes = [SMALLEST_ICON, SMALL_ICON, MEDIUM_ICON, LARGE_ICON, LARGEST_ICON]
    draw_row(draw, letters, sizes[0])

def draw_row(draw: ImageDraw, letters: str, size: int, y: int = 0):
    x = 0
    for letter in letters:
        icon = DayOfWeekIcon(letter, size)
        icon.draw(draw, x, y)
        x += size + GAP

def main():
    image = Image.new(mode="P", size=(500, 500), color=0)
    draw = ImageDraw.Draw(image)
    draw_icons(draw)
    palette = [
        255, 255, 255,  # 0 = WHITE
        0, 0, 0,  # 1 = BLACK
        255, 255, 0  # 2 = YELLOW
    ]
    image.putpalette(palette)
    converted = image.convert(mode="RGB")
    converted.show()

if __name__ == "__main__":
    main()
