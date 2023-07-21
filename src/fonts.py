from dataclasses import dataclass

from PIL import ImageFont
from font_roboto import RobotoBold


class Font:
    def __init__(self, size: int):
        self._font = ImageFont.truetype(font=RobotoBold, size=size)

    @property
    def family(self) -> str:
        return self._font.font.family

    @property
    def style(self) -> str:
        return self._font.font.style

    def height(self, text: str) -> int:
        return self._font.getbbox(text)[3]

    def width(self, text: str) -> int:
        return self._font.getbbox(text)[2]

    def pil_font(self) -> ImageFont:
        return self._font
