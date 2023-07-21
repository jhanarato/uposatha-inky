import pytest

from fonts import Font

@pytest.fixture
def font():
    return Font(size=30)

def test_should_have_family(font):
    assert font.family == "Roboto"

def test_should_have_style(font):
    assert font.style == "Bold"

def test_should_have_size(font):
    assert font.size == 30

def test_should_measure_height_of_text(font):
    assert font.height("Hello") == 28

def test_should_measure_width_of_text(font):
    assert font.width("Hello") == 70