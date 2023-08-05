from icon_grid_demo import icon_row, shifted_grid, axis_coordinates


def test_shifted_grid():
    icons = shifted_grid("ABC")
    row_str = "".join([icon.letter for icon in icons])
    assert row_str == "ABCBCACAB"

def test_icon_rows():
    row = icon_row("ABC")
    result = "".join([icon.letter for icon in row])
    assert result == "ABC"

def test_axis_coordinates():
    assert axis_coordinates(position=3) == [0, 12, 24]
