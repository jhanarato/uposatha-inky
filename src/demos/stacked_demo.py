from bbox import BBox
from components import Rectangle, Circle
from layout import StackedLayout
from screen import Ink
from viewer import DrawingViewer
from views import Pane

with DrawingViewer(height=200, width=200) as draw:
    components = [
        Rectangle(50, 50, Ink.BLACK),
        Circle(40, Ink.WHITE, Ink.WHITE)
    ]

    bbox = BBox(left=100, top=100, right=200, bottom=200)
    layout = StackedLayout(bbox)
    pane = Pane(components, layout)
    pane.draw(draw)
