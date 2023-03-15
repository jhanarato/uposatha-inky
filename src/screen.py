from dataclasses import dataclass
from enum import Enum
from typing import Dict

class Colour(Enum):
    WHITE = 0
    BLACK = 1
    YELLOW = 2

@dataclass
class Palette:
    WHITE: int = 0
    BLACK: int = 1
    YELLOW: int = 2

@dataclass
class ImageConfig:
    def __init__(self):
        self.height = 300
        self.width = 400
        self.palette = Palette()

    height: int
    width:  int
    palette: Palette