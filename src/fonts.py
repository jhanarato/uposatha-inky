from dataclasses import dataclass

from PIL import Image, ImageFont, ImageDraw
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

@dataclass
class BBox:
    left: int
    top: int
    right: int
    bottom: int

def font_bbox(text: str, font: ImageFont) -> BBox:
    bbox = font.getbbox(text)
    return BBox(*bbox)

def image_bbox(text: str, font: ImageFont) -> BBox:
    image = Image.new(mode="P", size=(100, 100), color=0)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, 1, font)
    bbox = image.getbbox()
    return BBox(*bbox)

