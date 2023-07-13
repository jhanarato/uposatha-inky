from datetime import date

from PIL import Image, ImageDraw

from uposatha.elements import MoonPhase

from components import Text, HorizontalLine
from countdown import Countdown, IconCountMapping, Appearance
from content import NextUposatha
from layout import ScreenLayout
from screen import ImageConfig

GAP = 4
SMALLEST_ICON = 25
SMALL_ICON = 35
MEDIUM_ICON = 40
LARGE_ICON = 45
LARGEST_ICON = 80

def new_countdown(config: ImageConfig, today: date, uposatha_falls_on: date,
                  moon_phase: MoonPhase, fourteen_day: bool) -> Countdown:

    if fourteen_day:
        appearances = IconCountMapping[Appearance](14)
        appearances[8, 14] = Appearance(SMALL_ICON, 7, GAP)
        appearances[4, 7] = Appearance(MEDIUM_ICON, 7, GAP)
        appearances[2, 3] = Appearance(LARGE_ICON, 7, GAP)
        appearances[1] = Appearance(LARGEST_ICON, 7, GAP)
    else:
        appearances = IconCountMapping[Appearance](15)
        appearances[11, 15] = Appearance(SMALLEST_ICON, 5, GAP)
        appearances[8, 10] = Appearance(SMALL_ICON, 5, GAP)
        appearances[4, 7] = Appearance(MEDIUM_ICON, 8, GAP)
        appearances[2, 3] = Appearance(LARGE_ICON, 8, GAP)
        appearances[1] = Appearance(LARGEST_ICON, 8, GAP)

    return Countdown(config=config, appearances=appearances,
                     start=today, end=uposatha_falls_on, moon_phase=moon_phase)

def next_uposatha(content: NextUposatha) -> Image:
    config = ImageConfig()
    font_styles = config.font_styles
    palette = config.palette

    image = Image.new(
        mode="P",
        size=(config.width, config.height),
        color=config.palette.WHITE
    )

    draw = ImageDraw.Draw(image)

    components = [
        Text("Uposatha", font_styles.HEADING, palette.BLACK),
        HorizontalLine(length=300, thickness=2, colour=palette.BLACK),
        Text(content.date, font_styles.INFO, palette.BLACK),
        new_countdown(config, content.today, content.falls_on, content.moon_phase, content.fourteen_day),
        Text(content.details, font_styles.INFO, palette.BLACK),
    ]

    layout = ScreenLayout(config.height, config.width)

    for component in components:
        layout.add_space(20)
        layout.add_centred(component)

    for component, coordinates in zip(components, layout.coordinates(), strict=True):
        component.draw(draw, *coordinates)

    return image
