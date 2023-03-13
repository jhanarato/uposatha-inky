from dataclasses import dataclass
from typing import List, Tuple,Protocol
from enum import Enum, auto

class Align(Enum):
    LEFT = auto()
    CENTRE = auto()
    RIGHT = auto()

class ImageComponent(Protocol):
    def height(self) -> int: ...
    def width(self) -> int: ...
    def draw(self, x: int, y: int) -> None: ...

@dataclass
class ComponentFormat:
    component: ImageComponent
    align: Align
    space_after: int

class Layout:
    def __init__(self, screen_height: int, screen_width: int):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.components: List[Tuple[ImageComponent, Align]] = []

    def add(self, component: ImageComponent, align: Align, space_after: int = 0) -> None:
        self.components.append((component, align))

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
        for component, align in self.components:
            component.draw(x=self.align_x(component, align), y=0)
