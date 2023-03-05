import pytest

from layout import Layout
from images import Text, DrawingConfig


def test_add_centred_text():
    layout = Layout(DrawingConfig())
    text = Text("Happy Birthday")
    layout.add_text(text)
    assert layout.items[0].x == 76 # Given RobotoBold 32pt
