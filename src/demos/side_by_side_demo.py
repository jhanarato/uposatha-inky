from bbox import BBox
from components import Text
from fonts import Font
from layout import VerticalLayout
from screen import Ink
from viewer import DrawingViewer

HEIGHT = 170
WIDTH = 200
MIDDLE = WIDTH // 2

with DrawingViewer(height=HEIGHT, width=WIDTH) as draw:
    components = [
        Text("Line 1", Font("roboto-bold", 20), Ink.BLACK),
        Text("Line 2", Font("roboto-bold", 20), Ink.BLACK),
        Text("Line 3", Font("roboto-bold", 20), Ink.BLACK),
    ]

    left_bbox = BBox(top=0, left=0, bottom=HEIGHT, right=MIDDLE)
    left_layout = VerticalLayout.all_centered(left_bbox, components, spacing=20)

    right_bbox = BBox(top=0, left=MIDDLE, bottom=HEIGHT, right=WIDTH)
    right_layout = VerticalLayout.all_centered(right_bbox, components, spacing=20)

    for component, coordinates in zip(components, left_layout.coordinates(), strict=True):
        component.draw(draw, *coordinates)

    for component, coordinates in zip(components, right_layout.coordinates(), strict=True):
        component.draw(draw, *coordinates)
