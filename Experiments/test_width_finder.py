import pytest

from font_roboto import RobotoBold
from fontTools.ttLib import TTFont
from PIL import ImageFont

from Experiments.witdh_finder import get_text_width

# Approval test for refactoring.
def test_width_finder():
    text = 'This is a test'
    font = TTFont(RobotoBold)
    assert get_text_width(text, font, 12) == 69.029296875

def test_width_finder_equivalent_to_pillow_length():
    size = 30
    text = "H"

    ft_font = TTFont(RobotoBold)
    pil_font = ImageFont.truetype(RobotoBold, size)

    ft_width = get_text_width(text, ft_font, size)
    pil_width = pil_font.getlength(text)

    assert ft_width == pytest.approx(pil_width, 0.001)