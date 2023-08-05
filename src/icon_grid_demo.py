from collections import deque
from collections.abc import Iterator

from PIL import Image, ImageDraw

from components import DayOfWeekIcon

def image_width() -> int:
    return 100

def image_height() -> int:
    return 100

def icon_coordinates(icon_count: int, icon_size: int) -> Iterator[tuple[int, int]]:
    yield 0, 0

def create_icons(letters: str, size: int) -> Iterator[DayOfWeekIcon]:
    icons = deque([DayOfWeekIcon(letter, size) for letter in letters])
    for _ in range(len(letters)):
        yield from icons
        icons.rotate(-1)

def shifted_grid(letters: str, size: int) -> Iterator[list[DayOfWeekIcon]]:
    yield icon_row("ABC", 10)
    yield icon_row("BCA", 10)
    yield icon_row("CAB", 10)


def icon_row(letters: str, size: int) -> list[DayOfWeekIcon]:
    return [DayOfWeekIcon(letter, size) for letter in letters]

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