from PIL import Image, ImageDraw
from inky import auto

from screen import Ink


class DrawingViewer:
    def __init__(self, height: int, width: int, show: bool = True):
        self._image = Image.new(mode="P", size=(width, height), color=Ink.WHITE.value)

        self._palette = [
            255, 255, 255,  # 0 = WHITE
            0, 0, 0,  # 1 = BLACK
            255, 255, 0  # 2 = YELLOW
        ]

        self._show = show

    def __enter__(self) -> ImageDraw:
        return ImageDraw.Draw(self._image)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._show:
            try:
                self._view_on_inky()
            except RuntimeError:
                self._view_on_screen()

    def _view_on_inky(self):
        display = auto()
        display.set_border(display.WHITE)
        upside_down = self._image.rotate(180)
        display.set_image(upside_down)
        display.show()

    def _view_on_screen(self):
        self._image.putpalette(self._palette)
        converted = self._image.convert(mode="RGB")
        converted.show()
