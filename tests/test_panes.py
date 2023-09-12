from PIL.ImageDraw import ImageDraw

from bbox import BBox
from layout import VerticalLayout, Align
from views import Pane


class Drawn:
    def __init__(self, height: int, width: int):
        self._height = height
        self._width = width
        self.drawn = False
        self.xy = None

    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return self._width

    def draw(self, draw: ImageDraw, x: int, y: int) -> None:
        self.drawn = True
        self.xy = (x, y)


def test_should_draw_pane():
    bbox = BBox(top=20, left=50, bottom=100, right=100)

    components = [
        Drawn(height=10, width=20),
        Drawn(height=20, width=30),
        Drawn(height=60, width=10),
    ]

    layout = VerticalLayout(bbox, Align.CENTER, spacing=20)

    pane = Pane(components, layout)
    pane.draw(None)

    assert all(component.drawn for component in components)

    coords = [component.xy for component in components]
    assert coords == [(65, 20), (60, 50), (70, 90)]
