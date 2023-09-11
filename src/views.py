from typing import Protocol, Any

from PIL import ImageDraw

from bbox import BBox
from components import Text, HorizontalLine
from content import Content, Context
from countdown import IconCountMapping, Appearance, Countdown
from fonts import Font
from layout import VerticalLayout
from screen import Ink, WIDTH, HEIGHT


class View(Protocol):
    def show(self, draw: ImageDraw) -> None: ...


def select_view(context: Context) -> View:
    if context.holiday_today():
        return HolidayView(context)
    elif context.uposatha_today():
        return UposathaView(context)
    else:
        return BetweenUposathasView(context)


class Pane:
    def __init__(self, bbox: BBox, layout: VerticalLayout, components: list[Any]):
        pass


class UposathaView:
    def __init__(self, context: Context):
        pass

    def show(self, draw: ImageDraw) -> None:
        font = Font("roboto", 30)
        text = Text("Today is the uposatha", font, Ink.BLACK)
        text.draw(draw, 10, 10)


class HolidayView:
    def __init__(self, context: Context):
        pass

    def show(self, draw: ImageDraw) -> None:
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

    def __init__(self, context: Context):
        self._content = Content(context)

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

    def _appearances(self) -> IconCountMapping[Appearance]:
        if self._content.fourteen_day:
            return self._fourteen_day_appearance()
        else:
            return self._fifteen_day_appearance()

    def _components(self):
        return [
            Text("Uposatha", Font("roboto-bold", 30), Ink.BLACK),
            HorizontalLine(300, Ink.BLACK),
            Text(self._content.date, Font("roboto-bold", 24), Ink.BLACK),
            Countdown(
                self._appearances(),
                self._content.today,
                self._content.falls_on,
                self._content.moon_phase),
            Text(self._content.details, Font("roboto-bold", 24), Ink.BLACK),
        ]

    def show(self, draw: ImageDraw) -> None:
        bbox = BBox(top=0, left=0, bottom=HEIGHT, right=WIDTH)
        layout = VerticalLayout.all_centered(bbox, self._components(), spacing=20)
        coordinates = layout.coordinates()
        components = self._components()

        for component, coordinates in zip(components, coordinates, strict=True):
            component.draw(draw, *coordinates)
