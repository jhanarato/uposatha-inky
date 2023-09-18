from screen import Ink
from viewer import DrawingViewer
from views import MoonWords


def test_moon_words_has_height():
    text_plus_spacing = 28 + 28 + 15
    words = MoonWords("Full", "Moon", Ink.BLACK)
    assert words.height() == text_plus_spacing


def test_moon_words_has_width():
    widest_word = 77
    words = MoonWords("Full", "Moon", Ink.BLACK)
    assert words.width() == widest_word


def test_moon_words_draw():
    words = MoonWords("Full", "Moon", Ink.BLACK)
    with DrawingViewer(200, 200, show=False) as draw:
        words.draw(draw, 50, 50)
