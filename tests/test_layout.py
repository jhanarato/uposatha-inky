import pytest

from layout import Layout
from images import Text


def test_add_centred_text():
    layout = Layout()
    heading_text = Text("Heading")
    layout.add_text(heading_text)
    assert layout.items[0].x == 0
