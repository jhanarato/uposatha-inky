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

class Layout:
    def __init__(self, screen_height: int, screen_width: int):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.components: List[Tuple[ImageComponent, Align]] = []

    def add(self, component: ImageComponent, align: Align) -> None:
        self.components.append((component, align))

    def center_aligned_x(self, component: ImageComponent) -> int:
        return int((self.screen_width - component.width()) / 2)

    def right_aligned_x(self, component: ImageComponent) -> int:
        return int((self.screen_width - component.width()))

    def align_x(self, component: ImageComponent, align: Align) -> int:
        if align == Align.LEFT:
            return 0
        if align == Align.CENTRE:
            return self.center_aligned_x(component)
        if align == Align.RIGHT:
            return self.right_aligned_x(component)

    def draw(self) -> None:
        for component, align in self.components:
            component.draw(x=self.align_x(component, align), y=0)
