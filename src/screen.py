from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict

from PIL import ImageFont, ImageDraw
from font_roboto import RobotoBold

@dataclass
class Palette:
    WHITE: int = 0
    BLACK: int = 1
    YELLOW: int = 2

@dataclass
class FontStyles:
    HEADING: ImageFont = ImageFont.truetype(font=RobotoBold, size=36)
    INFO: ImageFont = ImageFont.truetype(font=RobotoBold, size=32)
    COUNTDOWN: ImageFont = ImageFont.truetype(font=RobotoBold, size=20)


@dataclass
class ImageConfig:
    height: int = 300
    width:  int = 400
    palette: Palette = Palette()
    font_styles: FontStyles = FontStyles()
