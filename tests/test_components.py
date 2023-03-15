import pytest

from PIL import Image, ImageDraw
from screen import ImageConfig
from components import Text


@pytest.fixture
def draw():
    config = ImageConfig()
    image = Image.new(mode="P", size=(config.width, config.height), color=config.palette.BLACK)
    return ImageDraw.Draw(image)

def test_text_width(draw):
    pass