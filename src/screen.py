from dataclasses import dataclass, field
from enum import Enum

from PIL import ImageFont
from font_roboto import RobotoBold

class Colour(Enum):
    WHITE = 0
    BLACK = 1
    YELLOW = 2


@dataclass
class FontStyles:
    HEADING: ImageFont = ImageFont.truetype(font=RobotoBold, size=30)
    INFO: ImageFont = ImageFont.truetype(font=RobotoBold, size=24)
    COUNTDOWN: ImageFont = ImageFont.truetype(font=RobotoBold, size=16)


@dataclass
class ImageConfig:
    height: int = 300
    width:  int = 400
    font_styles: FontStyles = field(default_factory=FontStyles)
