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

        ArrangedComponent(
            component=Text(
                draw=self._draw,
                text="Uposatha",
                font=self.config.font_styles.HEADING,
                colour=self.config.palette.BLACK
            ),
            align=Align.CENTRE
        )

        layout = ScreenLayout(screen_height=self.config.height,
                              screen_width=self.config.width)
        layout.add_space(20)

        layout.add_centred(
            Text(
                draw=self._draw,
                text="Uposatha",
                font=self.config.font_styles.HEADING,
                colour=self.config.palette.BLACK
            )
        )

        layout.add_space(20)

        layout.add_centred(
            HorizontalLine(
                draw=self._draw,
                length=300,
                thickness=2,
                colour=self.config.palette.BLACK
            )
        )

        layout.add_space(20)

        layout.add_centred(
            Text(
                draw=self._draw,
                text=content.date,
                font=self.config.font_styles.INFO,
                colour=self.config.palette.BLACK
            )
        )

        layout.add_space(20)

        icons = create_icons(
            draw=self._draw,
            config=self.config,
            size=20,
            letters=content.countdown
        )

        layout.add_centred(
            Countdown(icons=icons, gap=4)
        )

        layout.add_space(20)

        layout.add_centred(
            MultilineText(
                draw=self._draw,
                text=content.info,
                font=self.config.font_styles.INFO,
                colour=self.config.palette.BLACK
            )
        )

        layout.draw()

    @property
    def image(self):
        return self._image
