from bbox import BBox
from layout import VerticalLayout


class Area:
    def __init__(self, height: int, width: int):
        self._height = height
        self._width = width

    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return self._width


def test_should_draw_component_with_space_between():
    layout = VerticalLayout(BBox(top=0, left=0, bottom=100, right=200), default_spacing=30)

    components = [
        Area(10, 20),
        Area(10, 20),
    ]

    layout.add_all_centered(components)

    assert list(layout.coordinates()) == [(90, 30), (90, 70)]


def test_three_components_spaced():
    bbox = BBox(top=0, left=0, bottom=100, right=200)
    layout = VerticalLayout(bbox, default_spacing=50)

    components = [
        Area(height=20, width=20),
        Area(height=30, width=20),
        Area(height=40, width=20)
    ]

    layout.add_all_centered(components)

    assert list(layout.coordinates()) == [(90, 50), (90, 120), (90, 200)]


def test_should_centre_align_area():
    area = Area(height=10, width=20)
    bbox = BBox(top=0, left=0, bottom=100, right=200)
    layout = VerticalLayout(bbox)
    layout.add_centred(area)
    assert list(layout.coordinates()) == [(90, 0)]


def test_should_left_align_area():
    area = Area(height=10, width=20)
    bbox = BBox(top=0, left=0, bottom=100, right=200)
    layout = VerticalLayout(bbox)
    layout.add_left(area)
    assert list(layout.coordinates()) == [(0, 0)]


def test_should_right_align_area():
    area = Area(height=10, width=20)
    bbox = BBox(top=0, left=0, bottom=100, right=200)
    layout = VerticalLayout(bbox)
    layout.add_right(area)
    assert list(layout.coordinates()) == [(180, 0)]


def test_should_handle_no_components():
    bbox = BBox(top=0, left=0, bottom=100, right=200)
    layout = VerticalLayout(bbox)
    assert list(layout.coordinates()) == []


def test_should_layout_in_vertically_offset_bbox():
    bbox = BBox(top=100, left=0, bottom=200, right=200)
    layout = VerticalLayout(bbox, default_spacing=50)

    components = [
        Area(height=20, width=100),
        Area(height=30, width=100),
    ]

    layout.add_all_centered(components)

    assert list(layout.coordinates()) == [(50, 150), (50, 220)]


def test_should_align_left_to_bbox():
    bbox = BBox(top=0, left=100, bottom=300, right=200)
    layout = VerticalLayout(bbox)
    layout.add_left(Area(height=50, width=70))
    assert list(layout.coordinates()) == [(100, 0)]


def test_should_align_right_to_bbox():
    bbox = BBox(top=0, left=100, bottom=300, right=200)
    layout = VerticalLayout(bbox)
    layout.add_right(Area(height=50, width=70))
    assert list(layout.coordinates()) == [(130, 0)]


def test_should_align_center_to_bbox():
    bbox = BBox(top=0, left=100, bottom=300, right=200)
    layout = VerticalLayout(bbox, default_spacing=20)
    layout.add_centred(Area(height=50, width=70))
    assert list(layout.coordinates()) == [(115, 0)]


def test_should_add_centered_sequence_of_components():
    components = [
        Area(height=70, width=50),
        Area(height=70, width=50),
        Area(height=70, width=50),
    ]

    bbox = BBox(top=0, left=0, bottom=300, right=200)

    layout = VerticalLayout(bbox, default_spacing=20)
    layout.add_all_centered(components)

    assert list(layout.coordinates()) == [(75, 20), (75, 110), (75, 200)]
