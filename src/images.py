from PIL import Image, ImageDraw

from components import Text, HorizontalLine, MultilineText, Countdown, create_icons
from content import NextUposatha
from layout import ScreenLayout
from screen import ImageConfig


def draw_next_uposatha(content: NextUposatha) -> Image:
    config = ImageConfig()
    image = Image.new(mode="P", size=(config.width, config.height), color=config.palette.WHITE)
    draw = ImageDraw.Draw(image)

    layout = ScreenLayout(screen_height=config.height,
                          screen_width=config.width)
    layout.add_space(20)

    layout.add_centred(
        Text(
            draw=draw,
            text="Uposatha",
            font=config.font_styles.HEADING,
            colour=config.palette.BLACK
        )
    )

    layout.add_space(20)

    layout.add_centred(
        HorizontalLine(
            draw=draw,
            length=300,
            thickness=2,
            colour=config.palette.BLACK
        )
    )

    layout.add_space(20)

    layout.add_centred(
        Text(
            draw=draw,
            text=content.date,
            font=config.font_styles.INFO,
            colour=config.palette.BLACK
        )
    )

    layout.add_space(20)

    icons = create_icons(
        draw=draw,
        config=config,
        size=20,
        letters=content.countdown
    )

    layout.add_centred(
        Countdown(icons=icons, gap=4)
    )

    layout.add_space(20)

    layout.add_centred(
        MultilineText(
            draw=draw,
            text=content.info,
            font=config.font_styles.INFO,
            colour=config.palette.BLACK
        )
    )

    layout.draw()

    return image
