from PIL import ImageDraw

from components import Glyph
from screen import Ink
from viewer import ImageViewer


def v_line(draw: ImageDraw, x: int) -> None:
    draw.line([x, 0, x, 100], width=1, fill=Ink.BLACK.value)


def h_line(draw: ImageDraw, y: int) -> None:
    draw.line([0, y, 100, y], width=1, fill=Ink.BLACK.value)


def draw():
    with ImageViewer(100, 100) as image:
        draw = ImageDraw.Draw(image)

        glyph = Glyph("W", 60, Ink.BLACK)
        x = 50 - (glyph.width() // 2)
        y = 50 - (glyph.height() // 2)
        glyph.draw(draw, x, y)

        v_line(draw, x)
        v_line(draw, x + glyph.width())
        h_line(draw, y)
        h_line(draw, y + glyph.height())


if __name__ == "__main__":
    draw()
