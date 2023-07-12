from dataclasses import dataclass, field

import pytest

from layout import ScreenLayout

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


def test_should_draw_component_with_space_after():
    log = DrawLog()
    layout = ScreenLayout(screen_height=100, screen_width=200)

    layout.add_centred(LoggerComponent(10, 20, log))
    layout.add_space(30)
    layout.add_centred(LoggerComponent(10, 20, log))

    coords = list(layout.coordinates())
    assert coords[1][1] == 40

def test_should_draw_component_with_space_before():
    log = DrawLog()
    layout = ScreenLayout(screen_height=100, screen_width=200)

    layout.add_space(20)
    layout.add_centred(LoggerComponent(20, 50, log))
    layout.draw()

    assert log.pixels[0].y == 20


def test_three_components_spaced():
    log = DrawLog()
    layout = ScreenLayout(screen_height=100, screen_width=200)

    layout.add_centred(LoggerComponent(height=20, width=20, log=log))
    layout.add_space(50)
    layout.add_centred(LoggerComponent(height=30, width=20, log=log))
    layout.add_space(30)
    layout.add_centred(LoggerComponent(height=40, width=20, log=log))
    layout.draw()

    assert log.pixels[0].y == 0
    assert log.pixels[1].y == 70
    assert log.pixels[2].y == 130


def test_should_centre_align_component():
    log = DrawLog()
    component = LoggerComponent(height=10, width=20, log=log)
    layout = ScreenLayout(screen_height=100, screen_width=200)
    layout.add_centred(component)
    layout.draw()

    assert component.log.pixels[0].x == 90

def test_should_left_align_component():
    log = DrawLog()
    component = LoggerComponent(height=10, width=20, log=log)
    layout = ScreenLayout(screen_height=100, screen_width=200)
    layout.add_left(component)
    layout.draw()

    assert component.log.pixels[0].x == 0

def test_should_generate_coordinates():
    log = DrawLog()
    layout = ScreenLayout(screen_height=100, screen_width=200)

    layout.add_centred(LoggerComponent(height=20, width=20, log=log))
    layout.add_space(50)
    layout.add_centred(LoggerComponent(height=30, width=20, log=log))
    layout.add_space(30)
    layout.add_centred(LoggerComponent(height=40, width=20, log=log))

    coordinates = list(layout.coordinates())
    assert coordinates == [(90, 0), (90, 70), (90, 130)]
