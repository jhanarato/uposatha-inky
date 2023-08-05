import itertools
from collections import deque
from collections.abc import Iterator

from PIL import Image, ImageDraw

from components import DayOfWeekIcon

ICON_SIZE = 10
BORDER = 20
GAP = 2

def image_width() -> int:
    return 100

def image_height() -> int:
    return 100

def axis_coordinates(position: int) -> list[int]:
    return [(ICON_SIZE + GAP) * column for column in range(position)]

def shifted_grid(letters: str) -> Iterator[DayOfWeekIcon]:
    icons = deque(icon_row(letters))
    for _ in range(len(letters)):
        yield from icons
        icons.rotate(-1)

def icon_row(letters: str) -> list[DayOfWeekIcon]:
    return [DayOfWeekIcon(letter, ICON_SIZE) for letter in letters]

def draw_icons(draw: ImageDraw) -> None:
    icon = DayOfWeekIcon("S", 30)
    icon.draw(draw, 35, 35)

def main():
    width = image_width()
    height = image_height()

    image = Image.new(mode="P", size=(width, height), color=0)
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