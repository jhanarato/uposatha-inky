from collections.abc import Iterator, Iterable
from enum import Enum, auto
from typing import Protocol

from bbox import BBox


class Area(Protocol):
    def height(self) -> int: ...

    def width(self) -> int: ...


class Align(Enum):
    LEFT = auto()
    RIGHT = auto()
    CENTER = auto()


class VerticalLayout:
    def __init__(self, bbox: BBox, align: Align, spacing: int):
        self._default_spacing = spacing
        self._bbox = bbox
        self._y = bbox.top
        self._coordinates = []

    def add_all_left(self, areas: Iterable[Area]):
        for area in areas:
            self._add_left(area)
            self._add_space(self._default_spacing)

    def add_all_centered(self, areas: Iterable[Area]):
        for area in areas:
            self._add_centred(area)
            self._add_space(self._default_spacing)

    def add_all_right(self, areas: Iterable[Area]):
        for area in areas:
            self._add_right(area)
            self._add_space(self._default_spacing)

    def coordinates(self) -> Iterator[tuple[int, int]]:
        return iter(self._coordinates)

    def _add_space(self, height: int) -> None:
        self._y += height

    def _add_left(self, area: Area) -> None:
        x = self._bbox.left
        self._coordinates.append((x, self._y))
        self._y += area.height()

    def _add_right(self, area: Area) -> None:
        x = self._bbox.right - area.width()
        self._coordinates.append((x, self._y))
        self._y += area.height()

    def _add_centred(self, area: Area) -> None:
        x = self._bbox.left + ((self._bbox.width - area.width()) // 2)
        self._coordinates.append((x, self._y))
        self._y += area.height()
