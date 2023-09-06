from PIL import ImageDraw

from components import Text, HorizontalLine
from content import Context, next_uposatha_content, NextUposatha
from countdown import IconCountMapping, Appearance, Countdown
from fonts import Font
from layout import VerticalLayout
from screen import Ink, WIDTH, HEIGHT
from viewer import DrawingViewer


def between_uposathas(context: Context):
    between_view = BetweenUposathasView()
    with DrawingViewer(width=WIDTH, height=HEIGHT) as draw:
        between_view.show(draw, context)


def uposatha(context: Context):
    with DrawingViewer(width=WIDTH, height=HEIGHT) as draw:
        font = Font("roboto", 30)
        text = Text("Today is the uposatha", font, Ink.BLACK)
        text.draw(draw, 10, 10)


def holiday(context: Context):
    with DrawingViewer(width=WIDTH, height=HEIGHT) as draw:
        font = Font("roboto", 30)
        text = Text("Today is a holiday", font, Ink.BLACK)
        text.draw(draw, 10, 10)


class BetweenUposathasView:
    GAP = 4
    SMALLEST_ICON = 25
    SMALL_ICON = 35
    MEDIUM_ICON = 40
    LARGE_ICON = 45
    LARGEST_ICON = 80

    def _fifteen_day_appearance(self) -> IconCountMapping[Appearance]:
        appearances = IconCountMapping[Appearance](15)
        appearances[11, 15] = Appearance(self.SMALLEST_ICON, 5, self.GAP)
        appearances[8, 10] = Appearance(self.SMALL_ICON, 5, self.GAP)
        appearances[4, 7] = Appearance(self.MEDIUM_ICON, 8, self.GAP)
        appearances[2, 3] = Appearance(self.LARGE_ICON, 8, self.GAP)
        appearances[1] = Appearance(self.LARGEST_ICON, 8, self.GAP)
        return appearances

    def _fourteen_day_appearance(self) -> IconCountMapping[Appearance]:
        appearances = IconCountMapping[Appearance](14)
        appearances[8, 14] = Appearance(self.SMALL_ICON, 7, self.GAP)
        appearances[4, 7] = Appearance(self.MEDIUM_ICON, 7, self.GAP)
        appearances[2, 3] = Appearance(self.LARGE_ICON, 7, self.GAP)
        appearances[1] = Appearance(self.LARGEST_ICON, 7, self.GAP)
        return appearances

    def _appearances(self, content: NextUposatha) -> IconCountMapping[Appearance]:
        if content.fourteen_day:
            return self._fourteen_day_appearance()
        else:
            return self._fifteen_day_appearance()

    def _components(self, content: NextUposatha):
        return [
            Text("Uposatha", Font("roboto-bold", 30), Ink.BLACK),
            HorizontalLine(300, Ink.BLACK),
            Text(content.date, Font("roboto-bold", 24), Ink.BLACK),
            Countdown(
                self._appearances(content),
                content.today,
                content.falls_on,
                content.moon_phase),
            Text(content.details, Font("roboto-bold", 24), Ink.BLACK),
        ]

    def _layout(self, content: NextUposatha) -> VerticalLayout:
        layout = VerticalLayout(HEIGHT, WIDTH)

        for component in self._components(content):
            layout.add_space(20)
            layout.add_centred(component)

        return layout

    def show(self, draw: ImageDraw, context: Context):
        content = next_uposatha_content(context)
        for component, coordinates in zip(self._components(content), self._layout(content).coordinates(), strict=True):
            component.draw(draw, *coordinates)
