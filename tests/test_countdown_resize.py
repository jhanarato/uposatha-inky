from datetime import date

import pytest

from countdown import Appearance, appearance


@pytest.mark.parametrize(
    "days_inclusive,appears",
    [
        (15, Appearance(icon_size=30, max_columns=8, gap=4)),
        (8, Appearance(icon_size=30, max_columns=8, gap=4)),
        (7, Appearance(icon_size=40, max_columns=7, gap=4)),
        (4, Appearance(icon_size=40, max_columns=4, gap=4)),
        (3, Appearance(icon_size=80, max_columns=3, gap=4)),
    ]
)
def test_should_adjust_size_as_uposatha_gets_closer(days_inclusive, appears):
    assert appearance(date(2023, 1, 1), date(2023, 1, days_inclusive)) == appears
