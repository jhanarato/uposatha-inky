from icon_grid_demo import create_icons, icon_coordinates


def test_create_icons():
    icons = create_icons("ABC", 10)
    result = "".join([icon.letter for icon in icons])
    assert result == "ABC" + "BCA" + "CAB"

def test_coordinates():
    coords = list(icon_coordinates(icon_count=9, icon_size=10))
    assert coords == [(0, 0)]
