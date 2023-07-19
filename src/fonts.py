from dataclasses import dataclass

from PIL import ImageFont
from font_roboto import RobotoBold

@dataclass
class FontStyles:
    HEADING: ImageFont = ImageFont.truetype(font=RobotoBold, size=30)
    INFO: ImageFont = ImageFont.truetype(font=RobotoBold, size=24)
    COUNTDOWN: ImageFont = ImageFont.truetype(font=RobotoBold, size=16)
