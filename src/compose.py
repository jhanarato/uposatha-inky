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

    def new_countdown(self, letters: list[str]) -> Countdown:
        icons = create_icons(
            draw=self._draw,
            config=self._config,
            size=20,
            letters=letters
        )

        return Countdown(icons=icons, gap=4)

    def new_horizontal_line(self, length: int) -> HorizontalLine:
        return HorizontalLine(
            draw=self._draw,
            length=length,
            thickness=2,
            colour=self._foreground
    )

def next_uposatha(content: NextUposatha) -> Image:
    config = ImageConfig()
    image = Image.new(mode="P", size=(config.width, config.height), color=config.palette.WHITE)
    draw = ImageDraw.Draw(image)

    image = PillowImage()

    heading = image.new_heading_text("Uposatha")
    divider = image.new_horizontal_line(300)
    falls_on = image.new_info_text(content.date)
    countdown = image.new_countdown(content.countdown)
    details = image.new_info_text(content.details)

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
