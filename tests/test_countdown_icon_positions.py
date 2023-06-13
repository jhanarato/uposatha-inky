import pytest

from countdown import IconPositions

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
    positions = IconPositions(max_columns=4)
    positions.icon_count(icon_count)
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
    positions = IconPositions(max_columns=4)
    positions.icon_count(icon_count)
    assert positions.columns == columns

@pytest.mark.parametrize(
    "icon_count,empty",
    [
        (3, 0),
        (4, 0),
        (5, 3),
        (6, 2),
        (7, 1),
        (8, 0),
        (9, 3),
    ]
)
def test_should_calculate_blank_cells(icon_count, empty):
    positions = IconPositions(max_columns=4)
    positions.icon_count(icon_count)
    assert positions.empty == empty

def test_should_yield_positions_without_gap():
    positions = IconPositions(max_columns=2)
    positions.icon_count(4)
    positions.icon_size(10)
    assert list(positions) == [
        (0, 0), (10, 0),
        (0, 10), (10, 10),
    ]

def test_should_skip_empty_positions():
    positions = IconPositions(max_columns=2)
    positions.icon_count(3)
    positions.icon_size(10)
    assert list(positions) == [
        (10, 0), (0, 10), (10, 10),
    ]
