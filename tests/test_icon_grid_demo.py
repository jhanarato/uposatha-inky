from icon_grid_demo import create_icons

def test_create_icons():
    icons = create_icons("ABC", 10)
    result = "".join([icon.letter for icon in icons])
    assert result == "ABC" + "BCA" + "CAB"


