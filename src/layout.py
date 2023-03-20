from dataclasses import dataclass
from typing import List, Tuple, Protocol
from enum import Enum, auto

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

@dataclass
class ArrangedComponent:
    """ A component with its layout"""
    component: ImageComponent
    align: Align
    space_before: int
    space_after: int

class Layout:
    """ A layout of ImageComponents in an image """
    def __init__(self, screen_height: int, screen_width: int):
        self._screen_height = screen_height
        self._screen_width = screen_width
        self._arrangement: List[ArrangedComponent] = []

    def add(self, component: ArrangedComponent) -> None:
        """ Add a component to be arranged in the image """
        self._arrangement.append(component)

    def draw(self) -> None:
        """ Draw all components in the image """
        y = 0
        for arranged in self._arrangement:
            x = self._align_x(arranged.component, arranged.align)
            y += arranged.space_before

            arranged.component.draw(x, y)

            y += arranged.component.height()
            y += arranged.space_after

    def _align_x(self, component: ImageComponent, align: Align) -> int:
        x = 0
        if align == Align.LEFT:
            x = 0
        elif align == Align.CENTRE:
            x = int((self._screen_width - component.width()) / 2)
        elif align == Align.RIGHT:
            x = int((self._screen_width - component.width()))
        return x
