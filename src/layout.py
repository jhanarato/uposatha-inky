from collections.abc import Iterator
from typing import Protocol
from enum import Enum, auto


class Align(Enum):
    LEFT = auto()
    CENTRE = auto()
    RIGHT = auto()


class Area(Protocol):
    def height(self) -> int: ...
    def width(self) -> int: ...


class VerticalSpace:
    """ A blank area between components. """
    def __init__(self, height: 0):
        self._height = height

    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return 0


class ScreenLayout:
    """ A layout of ImageComponents on the full image """
    def __init__(self, screen_height: int, screen_width: int):
        self._screen_height = screen_height
        self._screen_width = screen_width
        self._y = 0
        self._coordinates = []

    def add_space(self, height: int) -> None:
        self._y += height

    def add_left(self, component: Area) -> None:
        x = 0
        self._coordinates.append((x, self._y))
        self._y += component.height()

    def add_right(self, component: Area) -> None:
        x = self._screen_width - component.width()
        self._coordinates.append((x, self._y))
        self._y += component.height()

    def add_centred(self, component: Area) -> None:
        x = (self._screen_width - component.width()) // 2
        self._coordinates.append((x, self._y))
        self._y += component.height()

    def coordinates(self) -> Iterator[tuple[int, int]]:
        return iter(self._coordinates)
