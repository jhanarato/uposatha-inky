from collections.abc import Sequence
from datetime import date

import pytest
from uposatha.elements import MoonPhase

from countdown import Icons, Countdown
from screen import ImageConfig


def test_icon_sequence_has_length():
    config = ImageConfig()
    icons = Icons(None, config, 1, ["M", "T", "W"], MoonPhase.FULL)
    assert len(icons) == 4

def test_icon_sequence_can_be_iterated_over():
    config = ImageConfig()
    icons = Icons(None, config, 1, ["M", "T", "W"], MoonPhase.FULL)
    for icon in icons:
        pass

def test_icon_sequence_can_be_accessed_by_index():
    config = ImageConfig()
    icons = Icons(None, config, 1, ["M", "T", "W"], MoonPhase.FULL)
    assert str(icons[0]) == "M"

def test_icon_instance_is_sequence():
    config = ImageConfig()
    icons = Icons(None, config, 1, ["M", "T", "W"], MoonPhase.FULL)
    assert isinstance(icons, Sequence)

def test_icon_sequence_can_be_reversed():
    config = ImageConfig()
    icons = Icons(None, config, 1, ["M", "T", "W"], MoonPhase.FULL)
    assert [str(icon) for icon in reversed(icons)] == ["*", "W", "T", "M"]

def test_should_convert_icon_collection_to_string():
    icons = Icons(None, ImageConfig(), 10, ["S", "M", "T", "W"], MoonPhase.FULL)
    assert str(icons) == "SMTW*"


@pytest.mark.parametrize(
    "start,end,seq",
    [
        (date(2010, 3, 26), date(2010, 4, 9), "FSSMTWTFSSMTWT*"),
        (date(2010, 3, 26), date(2010, 3, 27), "F*"),
        (date(2010, 3, 26), date(2010, 3, 26), "*"),
    ]
)
def test_letters(start, end, seq):
    countdown = Countdown(draw=None, config=ImageConfig(),
                          start=date(2010, 3, 26), end=date(2010, 4, 9),
                          moon_phase=MoonPhase.FULL,
                          icon_size=0, gap=0, max_columns=0)

    assert str(countdown) == "FSSMTWTFSSMTWT*"
