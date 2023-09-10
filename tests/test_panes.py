from bbox import BBox
from components import Text
from fonts import Font
from layout import VerticalLayout
from panes import Pane
from screen import Ink


def test_create_pane():
    bbox = BBox(0, 0, 100, 100)
    layout = VerticalLayout(bbox)
    components = [Text("Text to show", Font("roboto-bold", 30), Ink.BLACK)]
    pane = Pane(bbox, layout, components)
