from compose import next_uposatha
from screen import Ink, WIDTH, HEIGHT
from components import Text
from content import Context, next_uposatha_content
from fonts import Font
from viewer import DrawingViewer


def between_uposathas(context: Context):
    content = next_uposatha_content(context.today)
    next_uposatha(content)


def uposatha(context: Context):
    with DrawingViewer(width=WIDTH, height=HEIGHT) as draw:
        font = Font("roboto", 30)
        text = Text("Today is the uposatha", font, Ink.BLACK)
        text.draw(draw, 10, 10)


def holiday(context: Context):
    with DrawingViewer(width=WIDTH, height=HEIGHT) as draw:
        font = Font("roboto", 30)
        text = Text("Today is a holiday", font, Ink.BLACK)
        text.draw(draw, 10, 10)
