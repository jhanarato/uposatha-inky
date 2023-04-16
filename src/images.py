from typing import List, Tuple
from PIL import Image, ImageDraw

from components import Text, HorizontalLine, MultilineText, Countdown, create_icons
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
        layout.add(self.date(content.date))
        layout.add(self.countdown(content.countdown))
        layout.add(self.info(content.info))
        layout.draw()

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

    def date(self, text: str) -> ArrangedComponent:
        return ArrangedComponent(
            component=Text(
                draw=self._draw,
                text=text,
                font=self.config.font_styles.INFO,
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
        icons = create_icons(
            draw=self._draw,
            config=self.config,
            size=20,
            letters=letters
        )

        return ArrangedComponent(
            component=Countdown(icons=icons, gap=4),
            align=Align.CENTRE,
            space_before=0,
            space_after=20
        )
