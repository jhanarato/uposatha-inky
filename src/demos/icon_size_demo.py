from collections.abc import Iterator

from PIL import ImageDraw

from components import DayOfWeekIcon
from viewer import DrawingViewer

GAP = 4


def days(size: int) -> list[DayOfWeekIcon]:
    return [DayOfWeekIcon(letter, size, 3) for letter in "SMTWF"]


def positions(border: int, letter_count: int, sizes: list[int]) -> Iterator[tuple[int, int]]:
    largest_icon = max(sizes)
    y = border
    for size in sizes:
        x = border
        for _ in range(letter_count):
            center_offset = (largest_icon - size) // 2
            yield x + center_offset, y
            x += largest_icon + GAP
        y += size + GAP


def icons(letters: str, sizes: list[int]) -> Iterator[DayOfWeekIcon]:
    for size in sizes:
        for letter in letters:
            yield DayOfWeekIcon(letter, size, 3)


def draw_icons(draw: ImageDraw, border: int, letters: str, sizes: list[int]) -> None:
    i = icons(letters, sizes)
    p = positions(border, len(letters), sizes)
    for icon, position in zip(i, p, strict=True):
        icon.draw(draw, position[0], position[1])


def image_width(border: int, letters: str, sizes: list[int]):
    largest_icon = max(sizes)
    border_size = border * 2
    icons_width = len(letters) * largest_icon
    gap_width = (len(letters) - 1) * GAP
    return border_size + icons_width + gap_width


def image_height(border: int, sizes: list[int]):
    border_size = border * 2
    icons_height = sum(sizes)
    gap_height = (len(sizes) - 1) * GAP
    return border_size + icons_height + gap_height


def main():
    border = 20
    letters = "SMTWF"
    sizes = list(range(10, 80, 10))
    width = image_width(border, letters, sizes)
    height = image_height(border, sizes)

    with DrawingViewer(width=width, height=height) as drawing:
        draw_icons(drawing, border, letters, sizes)


if __name__ == "__main__":
    main()
