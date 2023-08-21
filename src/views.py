from enum import Enum, auto
from PIL import ImageDraw

from screen import Ink, WIDTH, HEIGHT
from components import Text
from content import Context
from fonts import Font
from viewer import DrawingViewer


class View(Enum):
    BETWEEN = auto()
    UPOSATHA = auto()
    HOLIDAY = auto()


def between_uposathas(context: Context):
    with DrawingViewer(width=WIDTH, height=HEIGHT) as draw:
        font = Font("roboto", 30)
        text = Text("Future Uposatha View", font, Ink.BLACK)
        text.draw(draw, 50, 50)


def uposatha(context: Context):
    with DrawingViewer(width=WIDTH, height=HEIGHT) as draw:
        font = Font("roboto", 30)
        text = Text("Uposatha Is Today View", font, Ink.BLACK)
        text.draw(draw, 50, 50)


def holiday(context: Context):
    with DrawingViewer(width=WIDTH, height=HEIGHT) as draw:
        font = Font("roboto", 30)
        text = Text("Holiday Today View", font, Ink.BLACK)
        text.draw(draw, 50, 50)

