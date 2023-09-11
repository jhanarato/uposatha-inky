from PIL.ImageDraw import ImageDraw

from bbox import BBox
from views import Pane


def test_pane_draws_component():
    class Drawn:
        def __init__(self):
            self.drawn = False

        def height(self) -> int:
            return 0

        def width(self) -> int:
            return 0

        def draw(self, draw: ImageDraw, x: int, y: int) -> None:
            self.drawn = True

    bbox = BBox(top=0, left=0, bottom=100, right=100)

    components = [
        Drawn(), Drawn(), Drawn(),
    ]

    pane = Pane(components, bbox)
    pane.draw(None)

    assert all(component.drawn for component in components)
