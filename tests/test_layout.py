from dataclasses import dataclass, field

import pytest

from layout import ScreenLayout, ArrangedComponent, Align

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
    layout = ScreenLayout(screen_height=100, screen_width=200)
    layout.add(
        ArrangedComponent(
            component=LoggerComponent(height=10, width=20, log=log),
            align=align
        )
    )

    layout.draw()
    assert component.log.pixels[0].x == x_coord

def test_should_draw_component_with_space_after():
    log = DrawLog()
    layout = ScreenLayout(screen_height=100, screen_width=200)
    arrangements = [
        ArrangedComponent(
            component=LoggerComponent(10, 20, log),
            align=Align.CENTRE
        ),
        ArrangedComponent(
            component=LoggerComponent(10, 20, log),
            align=Align.CENTRE
        ),
    ]

    layout.add(arrangements[0])
    layout.add_space(30)
    layout.add(arrangements[1])

    layout.draw()
    assert log.pixels[-1].y == 40

def test_should_draw_component_with_space_before():
    log = DrawLog()
    layout = ScreenLayout(screen_height=100, screen_width=200)
    component = ArrangedComponent(
        component=LoggerComponent(20, 50, log),
        align=Align.CENTRE
    )

    layout.add_space(20)
    layout.add(component)
    layout.draw()

    assert log.pixels[0].y == 20


def test_three_components_spaced():
    log = DrawLog()
    layout = ScreenLayout(screen_height=100, screen_width=200)
    layout.add(
        ArrangedComponent(
            component=LoggerComponent(height=20, width=20, log=log),
            align=Align.CENTRE
        )
    )

    layout.add_space(50)

    layout.add(
        ArrangedComponent(
            component=LoggerComponent(height=30, width=20, log=log),
            align=Align.CENTRE
        )
    )

    layout.add_space(30)

    layout.add(
        ArrangedComponent(
            component=LoggerComponent(height=40, width=20, log=log),
            align=Align.CENTRE
        )
    )

    layout.draw()

    assert log.pixels[0].y == 0
    assert log.pixels[1].y == 70
    assert log.pixels[2].y == 130

def test_should_space_using_component():
    log = DrawLog()
    layout = ScreenLayout(screen_height=100, screen_width=200)

    layout.add_space(height=10)

    layout.add(
        ArrangedComponent(
            component=LoggerComponent(height=20, width=20, log=log),
            align=Align.CENTRE
        )
    )

    layout.draw()

    assert log.pixels[0].y == 10
