from collections.abc import Iterable
from typing import Protocol

from PIL import ImageDraw

from bbox import BBox
from components import Text, HorizontalLine, Component
from content import Content, Context
from countdown import IconCountMapping, Appearance, Countdown
from fonts import Font
from layout import VerticalLayout, Align
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
    def __init__(self, components: Iterable[Component], layout: VerticalLayout):
        self._layout = layout
        self._components = components
        self._layout.add(components)

    def draw(self, draw: ImageDraw) -> None:
        coords = self._layout.coordinates()
        for component, coordinates in zip(self._components, coords, strict=True):
            component.draw(draw, *coordinates)


class UposathaView:
    def __init__(self, context: Context):
        pass

    def _components(self):
        return [
            Text("Uposatha Today", Font("roboto-bold", 30), Ink.BLACK),
            HorizontalLine(300, Ink.BLACK),
        ]

    def show(self, draw: ImageDraw) -> None:
        bbox = BBox(top=20, left=0, bottom=HEIGHT, right=WIDTH)
        layout = VerticalLayout(bbox, Align.CENTER, spacing=20)
        pane = Pane(self._components(), layout)
        pane.draw(draw)


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
            Text("Next Uposatha", Font("roboto-bold", 30), Ink.BLACK),
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
        bbox = BBox(top=20, left=0, bottom=HEIGHT, right=WIDTH)
        layout = VerticalLayout(bbox, Align.CENTER, spacing=20)
        pane = Pane(self._components(), layout)
        pane.draw(draw)
