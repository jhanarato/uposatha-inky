from PIL import Image, ImageDraw

from components import Text, HorizontalLine
from countdown import Countdown, IconCountMapping, Appearance
from content import NextUposatha
from fonts import Font
from layout import VerticalLayout
from screen import Ink, HEIGHT, WIDTH
from viewer import DrawingViewer

GAP = 4
SMALLEST_ICON = 25
SMALL_ICON = 35
MEDIUM_ICON = 40
LARGE_ICON = 45
LARGEST_ICON = 80


def fifteen_day_appearance():
    appearances = IconCountMapping[Appearance](15)
    appearances[11, 15] = Appearance(SMALLEST_ICON, 5, GAP)
    appearances[8, 10] = Appearance(SMALL_ICON, 5, GAP)
    appearances[4, 7] = Appearance(MEDIUM_ICON, 8, GAP)
    appearances[2, 3] = Appearance(LARGE_ICON, 8, GAP)
    appearances[1] = Appearance(LARGEST_ICON, 8, GAP)
    return appearances


def fourteen_day_appearance():
    appearances = IconCountMapping[Appearance](14)
    appearances[8, 14] = Appearance(SMALL_ICON, 7, GAP)
    appearances[4, 7] = Appearance(MEDIUM_ICON, 7, GAP)
    appearances[2, 3] = Appearance(LARGE_ICON, 7, GAP)
    appearances[1] = Appearance(LARGEST_ICON, 7, GAP)
    return appearances


def next_uposatha(content: NextUposatha) -> None:
    if content.fourteen_day:
        appearance = fourteen_day_appearance()
    else:
        appearance = fifteen_day_appearance()

    components = [
        Text("Uposatha", Font("roboto-bold", 30), Ink.BLACK),
        HorizontalLine(300, Ink.BLACK),
        Text(content.date, Font("roboto-bold", 24), Ink.BLACK),
        Countdown(appearance, content.today, content.falls_on, content.moon_phase),
        Text(content.details, Font("roboto-bold", 24), Ink.BLACK),
    ]

    layout = VerticalLayout(HEIGHT, WIDTH)

    for component in components:
        layout.add_space(20)
        layout.add_centred(component)

    with DrawingViewer(width=WIDTH, height=HEIGHT) as draw:
        for component, coordinates in zip(components, layout.coordinates(), strict=True):
            component.draw(draw, *coordinates)
