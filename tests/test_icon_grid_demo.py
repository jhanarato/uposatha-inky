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
        (20, 20), (52, 20), (84, 20),
        (20, 52), (52, 52), (84, 52),
        (20, 84), (52, 84), (84, 84)
    ]


def test_image_size():
    assert image_size(letter_count=3) == 134
