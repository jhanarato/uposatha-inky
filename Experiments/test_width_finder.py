from Experiments.witdh_finder import get_text_width


def test_width_finder():
    text = 'This is a test'
    assert get_text_width(text, 12) == 69.029296875