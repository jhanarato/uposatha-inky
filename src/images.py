from typing import List, Tuple
from PIL import Image, ImageDraw

from components import Text, HorizontalLine, MultilineText, Countdown
from content import NextUposatha
from layout import ScreenLayout, Align, ArrangedComponent
from screen import ImageConfig


class NextUposathaDrawing:
    def __init__(self, content: NextUposatha):
        self.config: ImageConfig = ImageConfig()
        self._image: Image = Image.new(mode="P",
                                       size=(self.config.width, self.config.height),
                                       color=self.config.palette.WHITE)
        self._draw: ImageDraw = ImageDraw.Draw(self._image)

        self.heading("Uposatha")

        layout = ScreenLayout(screen_height=self.config.height,
                              screen_width=self.config.width)
        layout.add(self.heading("Uposatha"))
        layout.add(self.underline())
        layout.add(self.info(content.info))
        layout.add(self.countdown(content.countdown))
        layout.draw()

        # self.draw_countdown(content.countdown)

    @property
    def image(self):
        return self._image

    def heading(self, text: str) -> ArrangedComponent:
        return ArrangedComponent(
            component=Text(
                draw=self._draw,
                text=text,
                font=self.config.font_styles.HEADING,
                colour=self.config.palette.BLACK
            ),
            align=Align.CENTRE,
            space_before=20,
            space_after=20
        )

    def underline(self) -> ArrangedComponent:
        return ArrangedComponent(
            component=HorizontalLine(
                draw=self._draw,
                length=300,
                thickness=2,
                colour=self.config.palette.BLACK
            ),
            align=Align.CENTRE,
            space_before=0,
            space_after=20
        )

    def info(self, text: str) -> ArrangedComponent:
        return ArrangedComponent(
            component=MultilineText(
                draw=self._draw,
                text=text,
                font=self.config.font_styles.INFO,
                colour=self.config.palette.BLACK
            ),
            align=Align.CENTRE,
            space_before=0,
            space_after=20
        )

    def countdown(self, letters: list[str]) -> ArrangedComponent:
        return ArrangedComponent(
            component=Countdown(
                draw=self._draw,
                letters=letters
            ),
            align=Align.CENTRE,
            space_before=0,
            space_after=20
        )

    def draw_countdown(self, letters: List[str]) -> None:
        centres = centre_points(
            y_coord=220,
            screen_width=self.config.width,
            spacing=20,
            number_of_points=len(letters)
        )

        for letter, centre in zip(letters, centres):
            self.draw_letter(letter, centre)

    def draw_letter(self, letter: str, centre: Tuple[int, int]):
        font = self.config.font_styles.COUNTDOWN
        self._draw.text(
            xy=centre,
            text=letter,
            font=font,
            fill=self.config.palette.BLACK
        )


def centre_points(y_coord: int,
                  screen_width: int,
                  spacing: int,
                  number_of_points: int) -> List[Tuple[int, int]]:

    points_width = (number_of_points - 1) * spacing
    left = (screen_width - points_width) / 2

    return [(round(left + (point_number * spacing)), y_coord)
            for point_number in range(number_of_points)]
