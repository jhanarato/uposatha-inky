from PIL import ImageDraw

from components import Glyph
from screen import Ink
from viewer import DrawingViewer


def v_line(draw: ImageDraw, x: int) -> None:
    draw.line([x, 0, x, 100], width=1, fill=Ink.BLACK.value)


def h_line(draw: ImageDraw, y: int) -> None:
    draw.line([0, y, 100, y], width=1, fill=Ink.BLACK.value)


def draw_glyph_in_frame():
    with DrawingViewer(100, 100) as drawing:
        glyph = Glyph("H", 60, Ink.BLACK)
        x = 50 - (glyph.width() // 2)
        y = 50 - (glyph.height() // 2)
        glyph.draw(drawing, x, y)

        v_line(drawing, x)
        v_line(drawing, x + glyph.width())
        h_line(drawing, y)
        h_line(drawing, y + glyph.height())


if __name__ == "__main__":
    draw_glyph_in_frame()
