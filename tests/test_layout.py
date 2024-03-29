import pytest

from bbox import BBox
from layout import VerticalLayout, Align, StackedLayout


class Area:
    def __init__(self, height: int, width: int):
        self._height = height
        self._width = width

    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return self._width


def test_should_draw_component_with_space_between():
    bbox = BBox(top=30, left=0, bottom=100, right=200)
    layout = VerticalLayout(bbox, Align.CENTER, spacing=30)

    components = [
        Area(10, 20),
        Area(10, 20),
    ]

    layout.add(components)

    assert list(layout.coordinates()) == [(90, 30), (90, 70)]


def test_should_centre_align_area():
    area = Area(height=10, width=20)
    bbox = BBox(top=0, left=0, bottom=100, right=200)
    layout = VerticalLayout(bbox, Align.CENTER, spacing=0)
    layout._add_centred(area)
    assert list(layout.coordinates()) == [(90, 0)]


def test_should_left_align_area():
    area = Area(height=10, width=20)
    bbox = BBox(top=0, left=0, bottom=100, right=200)
    layout = VerticalLayout(bbox, Align.LEFT, spacing=0)
    layout._add_left(area)
    assert list(layout.coordinates()) == [(0, 0)]


def test_should_right_align_area():
    area = Area(height=10, width=20)
    bbox = BBox(top=0, left=0, bottom=100, right=200)
    layout = VerticalLayout(bbox, Align.RIGHT, spacing=0)
    layout._add_right(area)
    assert list(layout.coordinates()) == [(180, 0)]


def test_should_handle_no_components():
    bbox = BBox(top=0, left=0, bottom=100, right=200)
    layout = VerticalLayout(bbox, Align.LEFT, spacing=0)
    assert list(layout.coordinates()) == []


def test_should_layout_in_vertically_offset_bbox():
    bbox = BBox(top=100, left=0, bottom=200, right=200)
    layout = VerticalLayout(bbox, Align.CENTER, spacing=50)

    components = [
        Area(height=20, width=100),
        Area(height=30, width=100),
    ]

    layout.add(components)

    assert list(layout.coordinates()) == [(50, 100), (50, 170)]


def test_should_align_left_to_bbox():
    bbox = BBox(top=0, left=100, bottom=300, right=200)
    layout = VerticalLayout(bbox, Align.LEFT, spacing=0)
    layout._add_left(Area(height=50, width=70))
    assert list(layout.coordinates()) == [(100, 0)]


def test_should_align_right_to_bbox():
    bbox = BBox(top=0, left=100, bottom=300, right=200)
    layout = VerticalLayout(bbox, Align.RIGHT, spacing=0)
    layout._add_right(Area(height=50, width=70))
    assert list(layout.coordinates()) == [(130, 0)]


def test_should_align_center_to_bbox():
    bbox = BBox(top=0, left=100, bottom=300, right=200)
    layout = VerticalLayout(bbox, Align.CENTER, spacing=20)
    layout._add_centred(Area(height=50, width=70))
    assert list(layout.coordinates()) == [(115, 0)]


def test_should_add_centered_sequence_of_components():
    components = [
        Area(height=70, width=50),
        Area(height=70, width=80),
        Area(height=70, width=100),
    ]

    bbox = BBox(top=20, left=0, bottom=300, right=200)

    layout = VerticalLayout(bbox, Align.CENTER, spacing=20)
    layout.add(components)

    assert list(layout.coordinates()) == [(75, 20), (60, 110), (50, 200)]


def test_should_add_left_aligned_sequence_of_components():
    components = [
        Area(height=70, width=50),
        Area(height=70, width=70),
        Area(height=70, width=90),
    ]

    bbox = BBox(top=20, left=0, bottom=300, right=200)

    layout = VerticalLayout(bbox, Align.LEFT, spacing=20)
    layout.add(components)

    assert list(layout.coordinates()) == [(0, 20), (0, 110), (0, 200)]


def test_should_add_right_aligned_sequence_of_components():
    components = [
        Area(height=70, width=50),
        Area(height=70, width=30),
        Area(height=70, width=10),
    ]

    bbox = BBox(top=20, left=0, bottom=300, right=200)

    layout = VerticalLayout(bbox, Align.RIGHT, spacing=20)
    layout.add(components)

    assert list(layout.coordinates()) == [(150, 20), (170, 110), (190, 200)]


@pytest.mark.parametrize(
    "area,coords",
    [
        (Area(width=70, height=30), (65, 35)),
        (Area(width=80, height=20), (60, 40)),
        (Area(width=10, height=50), (95, 25)),
        (Area(width=25, height=25), (88, 38)),
    ]
)
def test_should_position_area_at_center_of_screen(area, coords):
    bbox = BBox(top=0, left=0, bottom=100, right=200)
    layout = StackedLayout(bbox)
    layout.add([area])

    assert next(layout.coordinates()) == coords


def test_should_stack_centered_full_screen():
    components = [
        Area(height=30, width=70),
        Area(height=20, width=80),
        Area(height=50, width=10),
        Area(height=25, width=25),
    ]

    bbox = BBox(top=0, left=0, bottom=100, right=200)

    layout = StackedLayout(bbox)
    layout.add(components)

    assert list(layout.coordinates()) == [
        (65, 35), (60, 40), (95, 25), (88, 38),
    ]


@pytest.mark.parametrize(
    "area,coords",
    [
        (Area(width=70, height=30), (75, 85)),
        (Area(width=80, height=20), (70, 90)),
        (Area(width=10, height=50), (105, 75)),
        (Area(width=25, height=25), (98, 88)),
    ]
)
def test_should_position_area_at_center_of_bbox(area, coords):
    # Center == (110, 100)
    bbox = BBox(top=50, left=40, bottom=150, right=180)
    layout = StackedLayout(bbox)
    layout.add([area])

    assert next(layout.coordinates()) == coords
