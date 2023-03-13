from dataclasses import dataclass

@dataclass(frozen=True)
class ScreenConfig:
    height: int = 300
    width:  int = 400
    white:  int = 0
    black:  int = 1
    yellow: int = 2
