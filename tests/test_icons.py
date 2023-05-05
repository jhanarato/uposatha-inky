import pytest

from icons import Icons
from screen import ImageConfig


def test_icon_sequence_has_length():
    config = ImageConfig()
    icons = Icons(None, config, 1, ["M", "T", "W"])
    assert len(icons) == 3

def test_icon_collection_can_be_iterated_over():
    config = ImageConfig()
    icons = Icons(None, config, 1, ["M", "T", "W"])
    for icon in icons:
        pass

def test_icon_collection_can_be_accessed_by_index():
    config = ImageConfig()
    icons = Icons(None, config, 1, ["M", "T", "W"])
    assert icons[0].height() == 1
