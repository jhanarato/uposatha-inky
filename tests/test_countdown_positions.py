import pytest

from countdown import GridLayout

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
    positions = GridLayout()
    positions.max_columns(4)
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
    positions = GridLayout()
    positions.max_columns(4)
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
    positions = GridLayout()
    positions.max_columns(4)
    positions.icon_count(icon_count)
    assert positions.empty == empty

def test_should_yield_positions_without_gap():
    positions = GridLayout()
    positions.max_columns(2)
    positions.icon_count(4)
    positions.icon_size(10)
    assert list(positions) == [
        (0, 0), (10, 0),
        (0, 10), (10, 10),
    ]

def test_should_skip_empty_positions():
    positions = GridLayout()
    positions.max_columns(2)
    positions.icon_count(3)
    positions.icon_size(10)
    assert list(positions) == [
        (10, 0), (0, 10), (10, 10),
    ]

def test_should_yield_positions_with_gap():
    positions = GridLayout()
    positions.max_columns(2)
    positions.icon_count(4)
    positions.icon_size(10)
    positions.gap(2)
    assert list(positions) == [
        (0, 0), (12, 0),
        (0, 12), (12, 12),
    ]

def test_should_accept_starting_coordinates():
    positions = GridLayout()
    positions.max_columns(2)
    positions.icon_count(4)
    positions.icon_size(10)
    positions.gap(2)
    positions.start_at(6, 9)
    assert list(positions) == [
        (6, 9),
        (18, 9),
        (6, 21),
        (18, 21),
    ]

def test_should_report_total_height():
    positions = GridLayout()
    positions.icon_count(6)
    positions.max_columns(3)
    assert positions.rows == 2
    positions.icon_size(10)
    positions.gap(2)
    assert positions.total_height == (2 * 10) + 2

def test_should_report_total_width():
    positions = GridLayout()
    positions.icon_count(6)
    positions.max_columns(3)
    assert positions.columns == 3
    positions.icon_size(10)
    positions.gap(2)
    assert positions.total_width == (3 * 10) + (2 * 2)
