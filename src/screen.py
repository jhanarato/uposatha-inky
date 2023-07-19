from dataclasses import dataclass, field
from enum import Enum

from PIL import ImageFont
from font_roboto import RobotoBold

HEIGHT = 300
WIDTH = 400

class Colour(Enum):
    WHITE = 0
    BLACK = 1
    YELLOW = 2

@dataclass
class FontStyles:
    HEADING: ImageFont = ImageFont.truetype(font=RobotoBold, size=30)
    INFO: ImageFont = ImageFont.truetype(font=RobotoBold, size=24)
    COUNTDOWN: ImageFont = ImageFont.truetype(font=RobotoBold, size=16)
