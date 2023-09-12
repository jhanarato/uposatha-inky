from collections.abc import Iterator, Iterable
from typing import Protocol

from bbox import BBox


class Area(Protocol):
    def height(self) -> int: ...

    def width(self) -> int: ...


class VerticalLayout:
    def __init__(self, bbox: BBox, spacing: int):
        self._default_spacing = spacing
        self._bbox = bbox
        self._screen_height = bbox.height
        self._screen_width = bbox.width
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

    def _add_left(self, component: Area) -> None:
        x = self._bbox.left
        self._coordinates.append((x, self._y))
        self._y += component.height()

    def _add_right(self, component: Area) -> None:
        x = self._bbox.right - component.width()
        self._coordinates.append((x, self._y))
        self._y += component.height()

    def _add_centred(self, component: Area) -> None:
        x = self._bbox.left + ((self._bbox.width - component.width()) // 2)
        self._coordinates.append((x, self._y))
        self._y += component.height()
