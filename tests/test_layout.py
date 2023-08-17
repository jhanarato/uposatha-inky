from layout import ColumnLayout


class Area:
    def __init__(self, height: int, width: int):
        self._height = height
        self._width = width

    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return self._width


def test_should_draw_component_with_space_after():
    layout = ColumnLayout(screen_height=100, screen_width=200)
    layout.add_centred(Area(10, 20))
    layout.add_space(30)
    layout.add_centred(Area(10, 20))
    assert list(layout.coordinates()) == [(90, 0), (90, 40)]

def test_should_draw_component_with_space_before():
    layout = ColumnLayout(screen_height=100, screen_width=200)
    layout.add_space(20)
    layout.add_centred(Area(20, 50))
    assert list(layout.coordinates()) == [(75, 20)]

def test_three_components_spaced():
    layout = ColumnLayout(screen_height=100, screen_width=200)
    layout.add_centred(Area(height=20, width=20))
    layout.add_space(50)
    layout.add_centred(Area(height=30, width=20))
    layout.add_space(30)
    layout.add_centred(Area(height=40, width=20))
    assert list(layout.coordinates()) == [(90, 0), (90, 70), (90, 130)]

def test_should_centre_align_area():
    area = Area(height=10, width=20)
    layout = ColumnLayout(screen_height=100, screen_width=200)
    layout.add_centred(area)
    assert list(layout.coordinates()) == [(90, 0)]

def test_should_left_align_area():
    area = Area(height=10, width=20)
    layout = ColumnLayout(screen_height=100, screen_width=200)
    layout.add_left(area)
    assert list(layout.coordinates()) == [(0, 0)]

def test_should_generate_coordinates():
    layout = ColumnLayout(screen_height=100, screen_width=200)
    layout.add_centred(Area(height=20, width=20))
    layout.add_space(50)
    layout.add_centred(Area(height=30, width=20))
    layout.add_space(30)
    layout.add_centred(Area(height=40, width=20))

    coordinates = list(layout.coordinates())
    assert coordinates == [(90, 0), (90, 70), (90, 130)]

def test_should_handle_no_components():
    layout = ColumnLayout(screen_height=100, screen_width=200)
    assert list(layout.coordinates()) == []

def test_should_handle_space_only():
    layout = ColumnLayout(screen_height=100, screen_width=200)
    layout.add_space(50)
    assert list(layout.coordinates()) == []