from collections.abc import Sequence
import pytest

from icons import Icons
from screen import ImageConfig


def test_icon_sequence_has_length():
    config = ImageConfig()
    icons = Icons(None, config, 1, ["M", "T", "W"])
    assert len(icons) == 3

def test_icon_sequence_can_be_iterated_over():
    config = ImageConfig()
    icons = Icons(None, config, 1, ["M", "T", "W"])
    for icon in icons:
        pass

def test_icon_sequence_can_be_accessed_by_index():
    config = ImageConfig()
    icons = Icons(None, config, 1, ["M", "T", "W"])
    assert icons[0].letter == "M"

def test_icon_instance_is_sequence():
    config = ImageConfig()
    icons = Icons(None, config, 1, ["M", "T", "W"])
    assert isinstance(icons, Sequence)

def test_icon_sequence_can_be_reversed():
    config = ImageConfig()
    icons = Icons(None, config, 1, ["M", "T", "W"])
    assert [icon.letter for icon in reversed(icons)] == ["W", "T", "M"]
