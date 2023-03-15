from PIL import ImageDraw

from screen import ImageConfig

class Text:
    def __init__(self, draw: ImageDraw, config: ImageConfig, text: str):
        self._draw = draw
        self._text = text
        self._font = config.font_styles.HEADING
        self._colour = config.palette.BLACK

    def height(self) -> int:
        return self._font.getbbox(self._text)[3]

    def width(self) -> int:
        return self._font.getbbox(self._text)[2]

    def draw(self, x: int, y: int) -> None:
        self._draw.text(xy=(x, y),
                        text=self._text,
                        fill=self._colour,
                        font=self._font)

class Underline:
    pass

class MultilineText:
    pass

class Countdown:
    pass
