from large_moon import MoonWords
from screen import Ink


def test_moon_words_has_height():
    words = MoonWords("Full", "Moon", Ink.BLACK)
    assert words.height() == 28 + 28 + 15
