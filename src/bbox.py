from dataclasses import dataclass

from PIL import ImageFont

from fonts import text_image


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


def font_bbox(text: str, font: ImageFont) -> BBox:
    bbox = font.getbbox(text)
    return BBox(*bbox)


def image_bbox(text: str, font: ImageFont) -> BBox:
    image = text_image(text, font)
    bbox = image.getbbox()
    return BBox(bbox[0], bbox[1], bbox[2] - 1, bbox[3] - 1)
