import pytest

from PIL import Image

from screen import Ink
from colour_bbox import coloured_pixels


@pytest.fixture
def image():
    return Image.new(
        mode="P",
        size=(10, 10),
        color=Ink.WHITE.value
    )

# def test_leftmost(image):
#     pixels = image.load()
#     pixels[5, 0] = Ink.BLACK.value
#     assert leftmost(image, Ink.BLACK) == 5

def test_coloured_pixels(image):
    pixels = image.load()
    pixels[5, 0] = Ink.BLACK.value
    coloured = list(coloured_pixels(image, Ink.BLACK))
    assert coloured == [(5, 0)]
