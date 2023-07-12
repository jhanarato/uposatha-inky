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
        self._arrangement: list[tuple[Area, Align]] = []

    def add_space(self, height: int) -> None:
        self._arrangement.append((VerticalSpace(height=height), Align.CENTRE))

    def add_left(self, component: Area) -> None:
        self._arrangement.append((component, Align.LEFT))

    def add_right(self, component: Area) -> None:
        self._arrangement.append((component, Align.RIGHT))

    def add_centred(self, component: Area) -> None:
        self._arrangement.append((component, Align.CENTRE))

    def _align_x(self, area: Area, align: Align) -> int:
        x = 0
        if align == Align.LEFT:
            x = 0
        elif align == Align.CENTRE:
            x = (self._screen_width - area.width()) // 2
        elif align == Align.RIGHT:
            x = self._screen_width - area.width()
        return x

    def coordinates(self) -> Iterator[tuple[int, int]]:
        y = 0
        for area, align in self._arrangement:
            x = self._align_x(area, align)
            if not isinstance(area, VerticalSpace):
                yield x, y
            y += area.height()
