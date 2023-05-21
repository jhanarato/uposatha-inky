from PIL import Image, ImageDraw

from components import Text, HorizontalLine
from countdown import Countdown, countdown_letters
from content import NextUposatha
from layout import ScreenLayout
from screen import ImageConfig

class PillowImage:
    """ Wraps a Pillow Image and allows components to be created with less boilerplate. """
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
        return Countdown(
            draw=self._draw,
            config=self._config,
            icon_size=20,
            letters=letters,
            gap=4,
            max_columns=8)

    def new_horizontal_line(self, length: int) -> HorizontalLine:
        return HorizontalLine(
            draw=self._draw,
            length=length,
            thickness=2,
            colour=self._foreground
        )

    def height(self) -> int:
        return self._config.height

    def width(self) -> int:
        return self._config.width

    def pillow_image(self) -> Image:
        return self._image

def next_uposatha(content: NextUposatha) -> Image:
    image = PillowImage()

    components = [
        image.new_heading_text("Uposatha"),
        image.new_horizontal_line(300),
        image.new_info_text(content.date),
        image.new_countdown(content.countdown),
        image.new_info_text(content.details)
    ]

    layout = ScreenLayout(image.height(), image.width())

    for component in components:
        layout.add_space(20)
        layout.add_centred(component)

    layout.draw()

    return image.pillow_image()
