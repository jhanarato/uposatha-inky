from inky.auto import auto

from PIL import Image, ImageDraw, ImageFont
from font_fredoka_one import FredokaOne

def make_image() -> Image:
    image = Image.new(mode="P", size=(400, 300))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FredokaOne, 36)
    draw.text((0, 0), "*** TESTING***", 1, font)
    return image

def display_on_screen(image: Image) -> None:
    palette = [
        255, 255, 255, # 1 = WHITE
        0, 0, 0,       # 2 = BLACK
        255, 255, 0    # 3 = YELLOW
    ]
    image.putpalette(palette)
    converted = image.convert(mode="RGB")
    converted.show()

def display_on_inky(image: Image) -> None:
    display = auto()
    display.set_border(display.WHITE)
    display.set_image(image)
    display.show()

if __name__ == "__main__":
    image = make_image()
    display_on_inky(image)
    # display_on_screen(image)
