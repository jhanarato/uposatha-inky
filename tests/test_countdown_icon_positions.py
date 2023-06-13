import pytest

from countdown import IconPositions

def test_should_iterate_over_positions():
    positions = IconPositions(icon_count=4, max_columns=2)
    assert list(positions) == [(0, 0)]

@pytest.mark.parametrize(
    "icon_count,rows",
    [
        (3, 1),
        (4, 1),
        (5, 2),
        (6, 2),
        (9, 3),
    ]
)
def test_should_calculate_rows(icon_count, rows):
    positions = IconPositions(icon_count=icon_count, max_columns=4)
    assert positions.rows == rows

@pytest.mark.parametrize(
    "icon_count,columns",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 4),
        (6, 4),
    ]
)
def test_should_calculate_columns(icon_count, columns):
    positions = IconPositions(icon_count=icon_count, max_columns=4)
    assert positions.columns == columns
