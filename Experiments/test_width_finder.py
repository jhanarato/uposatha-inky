from font_roboto import RobotoBold
from fontTools.ttLib import TTFont

from Experiments.witdh_finder import get_text_width

# Approval test for refactoring.
def test_width_finder():
    text = 'This is a test'
    font = TTFont(RobotoBold)
    assert get_text_width(text, font, 12) == 69.029296875