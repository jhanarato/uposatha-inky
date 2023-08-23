from PIL import ImageDraw

from components import Glyph, Circle
from fonts import Font
from screen import Ink
from viewer import DrawingViewer

HEIGHT = 100
WIDTH = 100


def v_line(draw: ImageDraw, x: int) -> None:
    draw.line([x, 0, x, HEIGHT], width=1, fill=Ink.BLACK.value)


def h_line(draw: ImageDraw, y: int) -> None:
    draw.line([0, y, WIDTH, y], width=1, fill=Ink.BLACK.value)


def draw_glyph_in_frame():
    with DrawingViewer(height=HEIGHT, width=WIDTH) as drawing:
        center_x = WIDTH // 2
        center_y = HEIGHT // 2

        circle = Circle(80, fill=Ink.WHITE, outline=Ink.BLACK)
        circle_x = center_x - (circle.width() // 2)
        circle_y = center_y - (circle.height() // 2)

        circle.draw(drawing, circle_x, circle_y)

        glyph = Glyph("H", Font("roboto-bold", 60), Ink.BLACK)
        glyph_x = center_x - (glyph.width() // 2)
        glyph_y = center_y - (glyph.height() // 2)

        glyph.draw(drawing, glyph_x, glyph_y)

        v_line(drawing, glyph_x)
        v_line(drawing, glyph_x + glyph.width())
        h_line(drawing, glyph_y)
        h_line(drawing, glyph_y + glyph.height())


if __name__ == "__main__":
    draw_glyph_in_frame()
