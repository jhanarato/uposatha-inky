import pytest

from countdown import GridLayout, Appearance


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
    appearance = Appearance(icon_size=0, max_columns=4, gap=0)
    layout = GridLayout(appearance, icon_count)
    assert layout.rows == rows


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
    appearance = Appearance(icon_size=0, max_columns=4, gap=0)
    layout = GridLayout(appearance, icon_count)
    assert layout.columns == columns


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
def test_should_calculate_empty_positions(icon_count, empty):
    appearance = Appearance(icon_size=0, max_columns=4, gap=0)
    layout = GridLayout(appearance, icon_count)
    assert layout.empty == empty


def test_should_yield_coordinates_without_gap():
    appearance = Appearance(icon_size=10, max_columns=2, gap=0)
    layout = GridLayout(appearance, 4)
    assert list(layout.coordinates(0, 0)) == [
        (0, 0), (10, 0),
        (0, 10), (10, 10),
    ]


def test_should_skip_empty_positions():
    appearance = Appearance(icon_size=10, max_columns=2, gap=0)
    layout = GridLayout(appearance, 3)
    assert list(layout.coordinates(0, 0)) == [
        (10, 0), (0, 10), (10, 10),
    ]


def test_should_yield_coordinates_with_gap():
    appearance = Appearance(icon_size=10, max_columns=2, gap=2)
    layout = GridLayout(appearance, 4)
    assert list(layout.coordinates(0, 0)) == [
        (0, 0), (12, 0),
        (0, 12), (12, 12),
    ]


def test_should_accept_starting_coordinates():
    appearance = Appearance(icon_size=10, max_columns=2, gap=2)
    layout = GridLayout(appearance, 4)
    assert list(layout.coordinates(6, 9)) == [
        (6, 9),
        (18, 9),
        (6, 21),
        (18, 21),
    ]


def test_should_report_total_height():
    appearance = Appearance(icon_size=10, max_columns=3, gap=2)
    layout = GridLayout(appearance, 6)
    assert layout.rows == 2
    assert layout.total_height == (2 * 10) + 2


def test_should_report_total_width():
    appearance = Appearance(icon_size=10, max_columns=3, gap=2)
    layout = GridLayout(appearance, 6)
    assert layout.columns == 3
    assert layout.total_width == (3 * 10) + (2 * 2)
