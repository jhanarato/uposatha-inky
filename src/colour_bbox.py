from typing import Optional, Iterator

from PIL import Image

from screen import Ink

def coloured_pixels(image: Image, colour: Ink) -> Iterator[tuple[int, int]]:
    pixels = image.load()
    for column in range(image.size[0]):
        for row in range(image.size[1]):
            if pixels[column, row] == colour.value:
                yield column, row
