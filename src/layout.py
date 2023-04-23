from dataclasses import dataclass
from typing import Protocol
from enum import Enum, auto

@dataclass
class BoundingBox:
    top: int
    left: int
    height: int
    width: int

class Align(Enum):
    LEFT = auto()
    CENTRE = auto()
    RIGHT = auto()

class ImageComponent(Protocol):
    """ Part of a large image to be placed by the layout """
    def height(self) -> int: ...
    """ Distance from the highest point to the lowest point"""

    def width(self) -> int: ...
    """ Distance from the leftmost point to the rightmost point """

    def draw(self, x: int, y: int) -> None: ...
    """ Draw given the top left coordinates """


class Space:
    """ A blank area between components. """
    def __init__(self, height: 0):
        self._height = height

    def height(self) -> int:
        return self._height

    def width(self) -> int:
        return 0

    def draw(self, x: int, y: int) -> None:
        pass


@dataclass
class ArrangedComponent:
    """ A component with its layout"""
    component: ImageComponent
    align: Align

class ScreenLayout:
    """ A layout of ImageComponents on the full image """
    def __init__(self, screen_height: int, screen_width: int):
        self._screen_height = screen_height
        self._screen_width = screen_width
        self._arrangement: list[ArrangedComponent] = []

    def add_space(self, height: int) -> None:
        component = ArrangedComponent(
            component=Space(height=height),
            align=Align.CENTRE
        )
        self._arrangement.append(component)

    def add_left(self, component: ImageComponent) -> None:
        arranged = ArrangedComponent(component, Align.LEFT)
        self._arrangement.append(arranged)

    def add_right(self, component: ImageComponent) -> None:
        arranged = ArrangedComponent(component, Align.RIGHT)
        self._arrangement.append(arranged)

    def add_centred(self, component: ImageComponent) -> None:
        arranged = ArrangedComponent(component, Align.CENTRE)
        self._arrangement.append(arranged)

    def draw(self) -> None:
        """ Draw all components in the image """
        y = 0
        for arranged in self._arrangement:
            x = self._align_x(arranged.component, arranged.align)
            arranged.component.draw(x, y)
            y += arranged.component.height()

    def _align_x(self, component: ImageComponent, align: Align) -> int:
        x = 0
        if align == Align.LEFT:
            x = 0
        elif align == Align.CENTRE:
            x = (self._screen_width - component.width()) // 2
        elif align == Align.RIGHT:
            x = self._screen_width - component.width()
        return x

XY = tuple[int, int]

class CountdownLayout:
    """ A sub-layout for countdown icons"""
    def __init__(self, bbox: BoundingBox, icons: list[ImageComponent], gap: int = 0):
        self._bbox = bbox
        self._icons = icons
        self._gap = gap
        self._offset = self._spacing() // 2
        self._x_start = self._bbox.left + self._offset
        self._y_start = self._bbox.top + self._offset

    def _spacing(self) -> int:
        return max_width(self._icons) + self._gap

    def _centers(self) -> list[XY]:
        return [(self._x_start + self._spacing() * icon_number, self._y_start)
                for icon_number in range(len(self._icons))]

    def _to_xy(self, centers: list[XY]) -> list[XY]:
        return [(cx - self._offset, cy - self._offset)
                for cx, cy in centers]

    def draw(self):
        icons_centers = self._centers()
        icons_xy = self._to_xy(icons_centers)
        for icon, xy in zip(self._icons, icons_xy):
            icon.draw(*xy)

def max_width(components: list[ImageComponent]) -> int:
    if not components:
        return 0

    return max(components, key=lambda component: component.width()).width()
