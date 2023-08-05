from icon_grid_demo import icon_row, shifted_grid, grid_coordinates, image_size


def test_shifted_grid():
    icons = shifted_grid("ABC")
    row_str = "".join([icon.letter for icon in icons])
    assert row_str == "ABCBCACAB"

def test_icon_rows():
    row = icon_row("ABC")
    result = "".join([icon.letter for icon in row])
    assert result == "ABC"

def test_grid_coordinates():
    assert list(grid_coordinates(3)) == [
        (20, 20), (32, 20), (44, 20),
        (20, 32), (32, 32), (44, 32),
        (20, 44), (32, 44), (44, 44)
    ]

def test_image_size():
    assert image_size(letter_count=3) == 74
