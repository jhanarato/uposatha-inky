from PIL import Image, ImageDraw

from components import DayOfWeekIcon
from compose import SMALLEST_ICON, SMALL_ICON, MEDIUM_ICON, LARGE_ICON, LARGEST_ICON, GAP

border = 20
letters = "SMTWF"
sizes = [SMALLEST_ICON, SMALL_ICON, MEDIUM_ICON, LARGE_ICON, LARGEST_ICON]

def days(size: int) -> list[DayOfWeekIcon]:
    return [DayOfWeekIcon(letter, size) for letter in "SMTWF"]

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

def main():
    border_size = border * 2
    icons_width = len(letters) * LARGEST_ICON
    gap_width = (len(letters) - 1) * GAP
    width = border_size + icons_width + gap_width
    height = 500
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
