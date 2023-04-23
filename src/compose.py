from PIL import Image, ImageDraw

from components import Text, HorizontalLine
from countdown import create_icons, Countdown
from content import NextUposatha
from layout import ScreenLayout
from screen import ImageConfig


def next_uposatha(content: NextUposatha) -> Image:
    config = ImageConfig()
    image = Image.new(mode="P", size=(config.width, config.height), color=config.palette.WHITE)
    draw = ImageDraw.Draw(image)

    heading = Text(
            draw=draw,
            text="Uposatha",
            font=config.font_styles.HEADING,
            colour=config.palette.BLACK
    )

    divider = HorizontalLine(
            draw=draw,
            length=300,
            thickness=2,
            colour=config.palette.BLACK
    )

    falls_on = Text(
            draw=draw,
            text=content.date,
            font=config.font_styles.INFO,
            colour=config.palette.BLACK
        )

    icons = create_icons(
        draw=draw,
        config=config,
        size=20,
        letters=content.countdown
    )

    countdown = Countdown(icons=icons, gap=4)

    details = Text(
        draw=draw,
        text=content.details,
        font=config.font_styles.INFO,
        colour=config.palette.BLACK)

    components = [
        heading,
        divider,
        falls_on,
        countdown,
        details
    ]

    layout = ScreenLayout(screen_height=config.height,
                          screen_width=config.width)

    for component in components:
        layout.add_space(20)
        layout.add_centred(component)

    layout.draw()

    return image
