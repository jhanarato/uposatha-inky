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
        self.center(component)
        self.components.append(component)

    def center(self, component: ImageComponent):
        pass
        # text.x = round((self._drawing.width - text.width) / 2)

    def draw(self):
        for component in self.components:
            component.draw(x=90, y=0)
