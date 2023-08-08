from dataclasses import dataclass


@dataclass
class BBox:
    left: int
    top: int
    right: int
    bottom: int

    @property
    def height(self) -> int:
        return self.bottom - self.top + 1

    @property
    def width(self) -> int:
        return self.right - self.left + 1

    @property
    def center(self) -> tuple[int, int]:
        x = self.left + self.width // 2
        y = self.top + self.height // 2
        return x, y
