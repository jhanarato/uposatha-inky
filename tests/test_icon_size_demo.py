from icon_size_demo import positions, image_width, image_height


def test_positions():
    border = 20
    sizes = [20, 30, 40]
    letter_count = 2
    expected = [(30, 20), (74, 20), (25, 44), (69, 44), (20, 78), (64, 78)]
    assert list(positions(border, letter_count, sizes)) == expected


def test_image_width():
    assert image_width(20, "abc", [10, 20, 30]) == 138


def test_image_height():
    assert image_height(20, [10, 20, 30]) == 108
