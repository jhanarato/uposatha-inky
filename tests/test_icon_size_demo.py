from icon_size_demo import positions


def test_positions():
    sizes = [10]
    border = 20
    assert list(positions(border, sizes)) == [(20, 20)]