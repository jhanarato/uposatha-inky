import pytest

from font_roboto import RobotoBold
from fontTools.ttLib import TTFont
from PIL import ImageFont

from fonts_x import pixel_width

# Approval test for refactoring. I just switched the
# font in the original script, the value is what was returned
# before I changed anything else.
def test_pixel_width():
    text = 'This is a test'
    font = TTFont(RobotoBold)
    assert pixel_width(text, font, 12) == 69.029296875

def test_pixel_width_equivalent_to_pillow_length():
    size = 30
    text = "H"

    ft_font = TTFont(RobotoBold)
    pil_font = ImageFont.truetype(RobotoBold, size)

    ft_width = pixel_width(text, ft_font, size)
    pil_width = pil_font.getlength(text)

    assert ft_width == pytest.approx(pil_width, 0.001)