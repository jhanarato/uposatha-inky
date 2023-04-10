import pytest

from components import LetterIcon


def test_should_centre_letter_text():
    icon = LetterIcon(draw=None, letter="W", size=40)
    icon._text_height = 10
    icon._text_width = 20
    assert icon._to_text_xy(0, 0) == (10, 15)
