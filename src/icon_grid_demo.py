from collections import deque
from collections.abc import Iterator

from PIL import Image, ImageDraw

from components import DayOfWeekIcon
from viewer import ImageViewer

ICON_SIZE = 30
BORDER = 20
GAP = 2


def image_size(letter_count: int) -> int:
    icon_space = ICON_SIZE * letter_count
    gap_space = GAP * (letter_count - 1)
    borders = 2 * BORDER
    return icon_space + gap_space + borders


def axis_coordinates(position: int) -> list[int]:
    return [(ICON_SIZE + GAP) * column for column in range(position)]


def grid_coordinates(grid_size: int) -> Iterator[tuple[int, int]]:
    for row in range(grid_size):
        for column in range(grid_size):
            x = BORDER + ((ICON_SIZE + GAP) * column)
            y = BORDER + ((ICON_SIZE + GAP) * row)
            yield x, y


def shifted_grid(letters: str) -> Iterator[DayOfWeekIcon]:
    icons = deque(icon_row(letters))
    for _ in range(len(letters)):
        yield from icons
        icons.rotate(-1)


def icon_row(letters: str) -> list[DayOfWeekIcon]:
    return [DayOfWeekIcon(letter, ICON_SIZE) for letter in letters]


def draw_icons(draw: ImageDraw, letters: str) -> None:
    coords = grid_coordinates(len(letters))
    icons = shifted_grid(letters)

    for xy, icon in zip(coords, icons):
        icon.draw(draw, xy[0], xy[1])


def main():
    letters = "SMTWF"
    size = image_size(len(letters))

    with ImageViewer(size, size) as image:
        draw = ImageDraw.Draw(image)
        draw_icons(draw, letters)


if __name__ == "__main__":
    main()
