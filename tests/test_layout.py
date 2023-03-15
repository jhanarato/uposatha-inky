import pytest

from layout import Layout, ImageComponent, Align


class FakeComponent(ImageComponent):
    def __init__(self, height: int, width: int):
        self._height = height
        self._width = width
        self.drawn_at_x = None
        self.drawn_at_y = None


    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return self._width

    def draw(self, x: int, y: int) -> None:
        self.drawn_at_x = x
        self.drawn_at_y = y

@pytest.mark.parametrize(
    "align,x_coord",
    [
        (Align.LEFT, 0),
        (Align.CENTRE, 90)
    ]
)
def test_should_align_component(align, x_coord):
    component = FakeComponent(height=10, width=20)
    layout = Layout(screen_height=100, screen_width=200)
    layout.add(component, align)
    layout.draw()
    assert component.drawn_at_x == x_coord

def test_should_space_component():
    layout = Layout(screen_height=100, screen_width=200)
    layout.add(
        component=FakeComponent(height=10, width=20),
        align=Align.CENTRE,
        space_after=30
    )

    layout.add(
        component=FakeComponent(height=10, width=20),
        align=Align.CENTRE,
        space_after=30
    )

    layout.draw()
    assert layout.components[-1][0].drawn_at_y == 40