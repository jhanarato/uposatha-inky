from collections.abc import Sequence
from datetime import date

import pytest
from uposatha.elements import MoonPhase

from countdown import Icons
from screen import ImageConfig


def test_icon_sequence_has_length():
    icons = Icons(1, date(2023, 6, 5), date(2023, 6, 8), MoonPhase.FULL)
    assert len(icons) == 4

def test_icon_sequence_can_be_iterated_over():
    icons = Icons(1, date(2023, 6, 5), date(2023, 6, 7), MoonPhase.FULL)
    for icon in icons:
        pass

def test_icon_sequence_can_be_accessed_by_index():
    icons = Icons(1, date(2023, 6, 5), date(2023, 6, 7), MoonPhase.FULL)
    assert str(icons[0]) == "M"

def test_icon_instance_is_sequence():
    icons = Icons(1, date(2023, 6, 5), date(2023, 6, 7), MoonPhase.FULL)
    assert isinstance(icons, Sequence)

def test_should_convert_icon_collection_to_string():
    icons = Icons(10, date(2023, 6, 4), date(2023, 6, 8), MoonPhase.FULL)
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
    icons = Icons(0, start, end, MoonPhase.FULL)
    assert str(icons) == seq

def test_should_raise_error_when_index_too_large():
    icons = Icons(1, date(2023, 6, 5), date(2023, 6, 7), MoonPhase.FULL)
    with pytest.raises(IndexError):
        _ = icons[3]

def test_should_get_icon_at():
    icons = Icons(1, date(2023, 6, 5), date(2023, 6, 7), MoonPhase.FULL)
    assert str(icons[0]) == "M"
    assert str(icons[1]) == "T"
    assert str(icons[2]) == "*"

def test_should_not_allow_negative_index():
    icons = Icons(1, date(2023, 6, 5), date(2023, 6, 7), MoonPhase.FULL)
    with pytest.raises(IndexError):
        _ = icons[-1]
