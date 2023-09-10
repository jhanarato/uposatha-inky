from collections.abc import Iterator, Iterable
from typing import Protocol

from bbox import BBox


class Area(Protocol):
    def height(self) -> int: ...

    def width(self) -> int: ...


class VerticalLayout:
    def __init__(self, bbox: BBox):
        self._bbox = bbox
        self._screen_height = bbox.height
        self._screen_width = bbox.width
        self._y = bbox.top
        self._coordinates = []

    @classmethod
    def all_centered(cls, bbox: BBox, areas: Iterable[Area], spacing: int):
        layout = cls(bbox)
        for area in areas:
            layout.add_space(spacing)
            layout.add_centred(area)

        return layout

    def add_space(self, height: int) -> None:
        self._y += height

    def add_left(self, component: Area) -> None:
        x = self._bbox.left
        self._coordinates.append((x, self._y))
        self._y += component.height()

    def add_right(self, component: Area) -> None:
        x = self._bbox.right - component.width()
        self._coordinates.append((x, self._y))
        self._y += component.height()

    def add_centred(self, component: Area) -> None:
        x = self._bbox.left + ((self._bbox.width - component.width()) // 2)
        self._coordinates.append((x, self._y))
        self._y += component.height()

    def coordinates(self) -> Iterator[tuple[int, int]]:
        return iter(self._coordinates)
