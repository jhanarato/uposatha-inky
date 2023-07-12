from layout import ScreenLayout


class Area:
    def __init__(self, height: int, width: int):
        self._height = height
        self._width = width

    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return self._width


def test_should_draw_component_with_space_after():
    layout = ScreenLayout(screen_height=100, screen_width=200)
    layout.add_centred(Area(10, 20))
    layout.add_space(30)
    layout.add_centred(Area(10, 20))

    coords = list(layout.coordinates())

    assert coords[1][1] == 40

def test_should_draw_component_with_space_before():
    layout = ScreenLayout(screen_height=100, screen_width=200)
    layout.add_space(20)
    layout.add_centred(Area(20, 50))

    coords = list(layout.coordinates())

    assert coords[0][1] == 20

def test_three_components_spaced():
    layout = ScreenLayout(screen_height=100, screen_width=200)
    layout.add_centred(Area(height=20, width=20))
    layout.add_space(50)
    layout.add_centred(Area(height=30, width=20))
    layout.add_space(30)
    layout.add_centred(Area(height=40, width=20))

    coords = list(layout.coordinates())

    assert coords[0][1] == 0
    assert coords[1][1] == 70
    assert coords[2][1] == 130


def test_should_centre_align_component():
    component = Area(height=10, width=20)
    layout = ScreenLayout(screen_height=100, screen_width=200)
    layout.add_centred(component)

    coords = list(layout.coordinates())

    assert coords[0][0] == 90

def test_should_left_align_component():
    component = Area(height=10, width=20)
    layout = ScreenLayout(screen_height=100, screen_width=200)
    layout.add_left(component)

    coords = list(layout.coordinates())

    assert coords[0][0] == 0

def test_should_generate_coordinates():
    layout = ScreenLayout(screen_height=100, screen_width=200)
    layout.add_centred(Area(height=20, width=20))
    layout.add_space(50)
    layout.add_centred(Area(height=30, width=20))
    layout.add_space(30)
    layout.add_centred(Area(height=40, width=20))

    coordinates = list(layout.coordinates())
    assert coordinates == [(90, 0), (90, 70), (90, 130)]
