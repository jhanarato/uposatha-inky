from typing import List, Protocol

class ImageComponent(Protocol):
    def height(self) -> int: ...
    def width(self) -> int: ...
    def draw(self, x: int, y: int) -> None: ...

class Layout:
    def __init__(self, screen_height: int, screen_width: int):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.components: List[ImageComponent] = []

    def add(self, component: ImageComponent) -> None:
        self.components.append(component)

    def center_aligned_x(self, component: ImageComponent):
        return round(
            (self.screen_width - component.width()) / 2
        )

    def draw(self):
        for component in self.components:
            component.draw(x=self.center_aligned_x(component), y=0)
