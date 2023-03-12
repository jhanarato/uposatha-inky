import pytest

from layout import Layout, ImageComponent

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


def test_should_center_one_component():
    component = FakeComponent(height=10, width=20)
    layout = Layout(screen_height=100, screen_width=200)
    layout.add(component)
    layout.draw()
    assert component.drawn_at_x == 90

# def test_add_centred_text():
#     layout = Layout(DrawingConfig())
#     text = Text("Happy Birthday")
#     layout.add_text(text)
#     assert layout.items[0].x == 76 # Given RobotoBold 32pt

