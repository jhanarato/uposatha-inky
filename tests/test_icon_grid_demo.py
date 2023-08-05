from icon_grid_demo import create_icons, icon_coordinates, icon_row, shifted_grid


def test_create_icons():
    icons = create_icons("ABC", 10)
    result = "".join([icon.letter for icon in icons])
    assert result == "ABC" + "BCA" + "CAB"

def test_shifted_grid():
    rows = shifted_grid("ABC", 10)
    row_str = []
    for row in rows:
        row_str.append("".join([icon.letter for icon in row]))

    assert row_str == ["ABC", "BCA", "CAB"]

def test_icon_rows():
    row = icon_row("ABC", 10)
    result = "".join([icon.letter for icon in row])
    assert result == "ABC"

def test_coordinates():
    coords = list(icon_coordinates(icon_count=9, icon_size=10))
    assert coords == [(0, 0)]
