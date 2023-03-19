from dataclasses import dataclass, field

import pytest

from layout import Layout, ImageComponent, Align

@dataclass
class Pixel:
    x: int
    y: int

@dataclass
class DrawLog:
    pixels: list[Pixel] = field(default_factory=list)

class LoggerComponent:
    def __init__(self, height: int, width: int, log: DrawLog):
        self._height = height
        self._width = width
        self.log = log

    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return self._width

    def draw(self, x: int, y: int) -> None:
        self.log.pixels.append(Pixel(x, y))

@pytest.mark.parametrize(
    "align,x_coord",
    [
        (Align.LEFT, 0),
        (Align.CENTRE, 90)
    ]
)
def test_should_align_component(align, x_coord):
    log = DrawLog()
    component = LoggerComponent(height=10, width=20, log=log)
    layout = Layout(screen_height=100, screen_width=200)
    layout.add(component, align)
    layout.draw()
    assert component.log.pixels[0].x == x_coord

def test_should_space_component():
    log = DrawLog()
    layout = Layout(screen_height=100, screen_width=200)
    component_sizes = [
        (10, 20),
        (10, 20),
    ]

    for size in component_sizes:
        layout.add(LoggerComponent(size[0], size[1], log), align=Align.CENTRE, space_after=30)

    layout.draw()
    assert log.pixels[-1].y == 40
