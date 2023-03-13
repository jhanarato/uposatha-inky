import pytest

from PIL import Image, ImageDraw
from screen import ScreenConfig
from components import Text


@pytest.fixture
def draw():
    config = ScreenConfig()
    image = Image.new(mode="P", size=(config.width, config.height), color=config.black)
    return ImageDraw.Draw(image)

def test_text_width(draw):
    pass