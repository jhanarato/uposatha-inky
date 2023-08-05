from icon_grid_demo import icon_row, shifted_grid, axis_coordinates


def test_shifted_grid():
    rows = shifted_grid("ABC")
    row_str = []
    for row in rows:
        row_str.append("".join([icon.letter for icon in row]))

    assert row_str == ["ABC", "BCA", "CAB"]

def test_icon_rows():
    row = icon_row("ABC")
    result = "".join([icon.letter for icon in row])
    assert result == "ABC"

def test_axis_coordinates():
    assert axis_coordinates(position=3) == [0, 12, 24]
