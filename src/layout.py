from collections.abc import Iterator
from typing import Protocol

from bbox import BBox


class Area(Protocol):
    def height(self) -> int: ...

    def width(self) -> int: ...


class VerticalLayout:
    def __init__(self, bbox: BBox):
        self._screen_height = bbox.height
        self._screen_width = bbox.width
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
