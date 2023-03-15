from dataclasses import dataclass
from typing import List, Tuple,Protocol
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

class Layout:
    """ A layout of ImageComponents in an image """
    def __init__(self, screen_height: int, screen_width: int):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.components: List[Tuple[ImageComponent, Align, int]] = []

    def add(self, component: ImageComponent, align: Align, space_after: int = 0) -> None:
        self.components.append((component, align, space_after))

    def align_x(self, component: ImageComponent, align: Align) -> int:
        x = 0
        if align == Align.LEFT:
            x = 0
        elif align == Align.CENTRE:
            x = int((self.screen_width - component.width()) / 2)
        elif align == Align.RIGHT:
            x = int((self.screen_width - component.width()))
        return x

    def draw(self) -> None:
        y = 0
        for component, align, space_after in self.components:
            component.draw(x=self.align_x(component, align), y=y)
            y += component.height() + space_after
