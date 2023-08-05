from collections.abc import Iterator

from PIL import Image, ImageDraw

from components import DayOfWeekIcon
from compose import SMALLEST_ICON, SMALL_ICON, MEDIUM_ICON, LARGE_ICON, LARGEST_ICON, GAP


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

def icons(letters: str, sizes: list[int]) -> Iterator[DayOfWeekIcon]:
    for size in sizes:
        for letter in letters:
            yield DayOfWeekIcon(letter, size)

def draw_icons(draw: ImageDraw, border: int, letters: str, sizes: list[int]) -> None:
    i = icons(letters, sizes)
    p = positions(border, len(letters), sizes)
    for icon, position in zip(i, p, strict=True):
        icon.draw(draw, position[0], position[1])

def image_width(border: int, letters: str, sizes: list[int]):
    border_size = border * 2
    icons_width = len(letters) * LARGEST_ICON
    gap_width = (len(letters) - 1) * GAP
    return border_size + icons_width + gap_width


def image_height(border: int, letters: str, sizes: list[int]):
    border_size = border * 2
    icons_height = sum(sizes)
    gap_height = (len(sizes) - 1) * GAP
    return border_size + icons_height + gap_height

def main():
    border = 20
    letters = "SMTWF"
    sizes = [SMALLEST_ICON, SMALL_ICON, MEDIUM_ICON, LARGE_ICON, LARGEST_ICON]
    width = image_width(border, letters, sizes)
    height = image_height(border, letters, sizes)
    image = Image.new(mode="P", size=(width, height), color=0)
    draw = ImageDraw.Draw(image)
    draw_icons(draw, border, letters, sizes)
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
