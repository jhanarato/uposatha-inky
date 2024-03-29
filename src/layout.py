from collections.abc import Iterator, Iterable
from enum import Enum, auto
from typing import Protocol

from bbox import BBox


class Area(Protocol):
    def height(self) -> int: ...

    def width(self) -> int: ...


class Layout(Protocol):
    def add(self, areas: Iterable[Area]) -> None: ...

    def coordinates(self) -> Iterator[tuple[int, int]]: ...


class Align(Enum):
    LEFT = auto()
    RIGHT = auto()
    CENTER = auto()


class VerticalLayout:
    def __init__(self, bbox: BBox, align: Align, spacing: int):
        self._bbox = bbox
        self._spacing = spacing
        self._align = align
        self._y = bbox.top
        self._coordinates = []

    def add(self, areas: Iterable[Area]) -> None:
        for area in areas:
            match self._align:
                case Align.LEFT:
                    self._add_left(area)
                case Align.RIGHT:
                    self._add_right(area)
                case Align.CENTER:
                    self._add_centred(area)

            self._add_space()

    def coordinates(self) -> Iterator[tuple[int, int]]:
        return iter(self._coordinates)

    def _add_space(self) -> None:
        self._y += self._spacing

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


class StackedLayout:
    def __init__(self, bbox: BBox):
        self._bbox = bbox
        self._coordinates = []

    def add(self, areas: Iterable[Area]) -> None:
        for area in areas:
            x = self._bbox.left + (self._bbox.width - area.width()) // 2
            y = self._bbox.top + (self._bbox.height - area.height()) // 2
            self._coordinates.append((x, y))

    def coordinates(self) -> Iterator[tuple[int, int]]:
        return iter(self._coordinates)
