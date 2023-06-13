import pytest

from countdown import IconPositions

def test_should_iterate_over_positions():
    positions = IconPositions(icon_count=4, max_columns=2)
    assert list(positions) == [(0, 0)]

def test_should_report_number_of_rows():
    positions = IconPositions(icon_count=4, max_columns=2)
    assert positions.rows == 2