from collections.abc import Sequence

from icons import CountdownIcons
from screen import ImageConfig


def test_icon_sequence_has_length():
    config = ImageConfig()
    icons = CountdownIcons(None, config, 1, ["M", "T", "W"])
    assert len(icons) == 3

def test_icon_sequence_can_be_iterated_over():
    config = ImageConfig()
    icons = CountdownIcons(None, config, 1, ["M", "T", "W"])
    for icon in icons:
        pass

def test_icon_sequence_can_be_accessed_by_index():
    config = ImageConfig()
    icons = CountdownIcons(None, config, 1, ["M", "T", "W"])
    assert str(icons[0]) == "M"

def test_icon_instance_is_sequence():
    config = ImageConfig()
    icons = CountdownIcons(None, config, 1, ["M", "T", "W"])
    assert isinstance(icons, Sequence)

def test_icon_sequence_can_be_reversed():
    config = ImageConfig()
    icons = CountdownIcons(None, config, 1, ["M", "T", "W"])
    assert [str(icon) for icon in reversed(icons)] == ["W", "T", "M"]

def test_should_convert_icon_collection_to_string():
    icons = CountdownIcons(None, ImageConfig(), 10, ["S", "M", "T", "W"])
    assert str(icons) == "SMTW"
