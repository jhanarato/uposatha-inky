from collections.abc import Iterator

from PIL import Image, ImageDraw

from components import DayOfWeekIcon
from compose import SMALLEST_ICON, SMALL_ICON, MEDIUM_ICON, LARGE_ICON, LARGEST_ICON, GAP

border = 20
letters = "SMTWF"
sizes = [SMALLEST_ICON, SMALL_ICON, MEDIUM_ICON, LARGE_ICON, LARGEST_ICON]

def days(size: int) -> list[DayOfWeekIcon]:
    return [DayOfWeekIcon(letter, size) for letter in "SMTWF"]

def positions(border: int, letter_count: int, sizes: list[int]) -> Iterator[tuple[int, int]]:
    y = border
    for size in sizes:
        x = border
        for _ in range(letter_count):
            center_offset = (LARGEST_ICON - size) // 2
            yield x + center_offset, y
            x += LARGEST_ICON + GAP
        y += size + GAP

def draw_icons(draw: ImageDraw):
    y = border
    for size in sizes:
        x = border
        for letter in letters:
            icon = DayOfWeekIcon(letter, size)
            center_offset = (LARGEST_ICON - size) / 2
            icon.draw(draw, x + center_offset, y)
            x += LARGEST_ICON + GAP
        y += size + GAP

def image_width():
    border_size = border * 2
    icons_width = len(letters) * LARGEST_ICON
    gap_width = (len(letters) - 1) * GAP
    return border_size + icons_width + gap_width


def image_height():
    border_size = border * 2
    icons_height = sum(sizes)
    gap_height = (len(sizes) - 1) * GAP
    return border_size + icons_height + gap_height

def main():
    image = Image.new(mode="P", size=(image_width(), image_height()), color=0)
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
