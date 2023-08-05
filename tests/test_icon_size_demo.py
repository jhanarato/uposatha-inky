from icon_size_demo import positions, image_width, image_height


def test_positions():
    border = 20
    sizes = [20, 30, 40]
    letter_count = 2
    expected = [(50, 20), (134, 20), (45, 44), (129, 44), (40, 78), (124, 78)]
    assert list(positions(border, letter_count, sizes)) == expected

def test_image_width():
    assert image_width(20, "abc", [10, 20, 30]) == 288

def test_image_height():
    assert image_height(20, [10, 20, 30]) == 108