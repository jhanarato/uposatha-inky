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
    layout.add(component, align, 0, 0)
    layout.draw()
    assert component.log.pixels[0].x == x_coord

@dataclass
class Arrangement:
    height: int
    width: int
    align: Align
    space_before: int
    space_after: int

def test_should_draw_component_with_space_after():
    log = DrawLog()
    layout = Layout(screen_height=100, screen_width=200)
    arrangements = [
        Arrangement(height=10, width=20, align=Align.CENTRE, space_after=30, space_before=0),
        Arrangement(height=10, width=20, align=Align.CENTRE, space_after=30, space_before=0),
    ]

    for arrange in arrangements:
        layout.add(
            component=LoggerComponent(arrange.height, arrange.width, log),
            align=Align.CENTRE,
            space_after=arrange.space_after,
            space_before=arrange.space_before
        )

    layout.draw()
    assert log.pixels[-1].y == 40

def test_should_draw_component_with_space_before():
    log = DrawLog()
    layout = Layout(screen_height=100, screen_width=200)
    layout.add(LoggerComponent(20, 50, log), Align.CENTRE, space_before=20, space_after=0)
    layout.draw()
    assert log.pixels[0].y == 20
