from PIL import Image, ImageDraw

from components import Text, HorizontalLine
from countdown import create_icons, Countdown
from content import NextUposatha
from layout import ScreenLayout
from screen import ImageConfig

class PillowImage:
    def __init__(self):
        self._config = ImageConfig()

        self._foreground = self._config.palette.BLACK
        self._background = self._config.palette.WHITE

        self._image = Image.new(
            mode="P",
            size=(self._config.width, self._config.height),
            color=self._config.palette.WHITE
        )

        self._draw = ImageDraw.Draw(self._image)

    def new_heading_text(self, text: str) -> Text:
        return Text(
            draw=self._draw,
            text=text,
            font=self._config.font_styles.HEADING,
            colour=self._foreground
        )

    def new_info_text(self, text: str) -> Text:
        return Text(
            draw=self._draw,
            text=text,
            font=self._config.font_styles.INFO,
            colour=self._foreground
        )


def next_uposatha(content: NextUposatha) -> Image:
    config = ImageConfig()
    image = Image.new(mode="P", size=(config.width, config.height), color=config.palette.WHITE)
    draw = ImageDraw.Draw(image)

    image = PillowImage()

    heading = image.new_heading_text("Uposatha")

    divider = HorizontalLine(
            draw=image._draw,
            length=300,
            thickness=2,
            colour=config.palette.BLACK
    )

    falls_on = image.new_info_text(content.date)

    icons = create_icons(
        draw=image._draw,
        config=config,
        size=20,
        letters=content.countdown
    )

    countdown = Countdown(icons=icons, gap=4)

    details = Text(
        draw=image._draw,
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

    return image._image
