import pytest

from components import LetterIcon
from screen import ImageConfig


def test_should_centre_letter_text():
    config = ImageConfig()
    icon = LetterIcon(draw=None,
                      font=config.font_styles.COUNTDOWN,
                      background=config.palette.BLACK,
                      foreground=config.palette.WHITE,
                      letter="W", size=40)
    icon._text_height = 10
    icon._text_width = 20
    assert icon._to_text_xy(0, 0) == (10, 15)
