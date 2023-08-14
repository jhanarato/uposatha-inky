from PIL import Image, ImageDraw

from screen import Ink


class DrawingViewer:
    def __init__(self, height: int, width: int):
        self._height = height
        self._width = width

    def __enter__(self) -> ImageDraw:
        self._image = Image.new(
            mode="P",
            size=(self._width, self._height),
            color=Ink.WHITE.value
        )
        return ImageDraw.Draw(self._image)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            palette = [
                255, 255, 255,  # 0 = WHITE
                0, 0, 0,  # 1 = BLACK
                255, 255, 0  # 2 = YELLOW
            ]

            self._image.putpalette(palette)
            converted = self._image.convert(mode="RGB")
            converted.show()
