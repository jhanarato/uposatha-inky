from collections.abc import Iterable
from typing import Protocol

from PIL.ImageDraw import ImageDraw
from uposatha.elements import MoonPhase

from bbox import BBox
from components import Text, HorizontalLine, Component, Circle
from content import Content, Context
from countdown import IconCountMapping, Appearance, Countdown
from fonts import Font
from layout import VerticalLayout, Align, Layout, StackedLayout
from screen import Ink, WIDTH, HEIGHT


class View(Protocol):
    def show(self, draw: ImageDraw) -> None: ...


def select_view(context: Context) -> View:
    if context.holiday_today():
        return UposathaView(context)
    elif context.uposatha_today():
        return UposathaView(context)
    else:
        return BetweenUposathasView(context)


class Pane:
    def __init__(self, components: Iterable[Component], layout: Layout):
        self._layout = layout
        self._components = components
        self._layout.add(components)

    def draw(self, draw: ImageDraw) -> None:
        coords = self._layout.coordinates()
        for component, coordinates in zip(self._components, coords, strict=True):
            component.draw(draw, *coordinates)


class MoonWords:
    def __init__(self, first_word: str, second_word: str, colour: Ink):
        font = Font("roboto-bold", 28)
        self._first_text = Text(first_word, font, colour)
        self._second_text = Text(second_word, font, colour)
        self._spacing = 10

    def height(self) -> int:
        h = self._first_text.height()
        h += self._second_text.height()
        h += self._spacing
        return h

    def width(self) -> int:
        return max(self._first_text.width(), self._second_text.width())

    def draw(self, draw: ImageDraw, x: int, y: int) -> None:
        components = [self._first_text, self._second_text]
        bbox = BBox(
            left=x,
            right=x + self.width(),
            top=y,
            bottom=y + self.height()
        )
        layout = VerticalLayout(bbox, Align.CENTER, self._spacing)
        pane = Pane(components, layout)
        pane.draw(draw)


class UposathaView:
    def __init__(self, context: Context):
        self._content = Content(context)

    def _heading_pane(self) -> Pane:
        components = [
            Text("Uposatha Today", Font("roboto-bold", 30), Ink.BLACK),
            HorizontalLine(300, Ink.BLACK),
        ]

        bbox = BBox(top=20, left=0, bottom=95, right=WIDTH)
        layout = VerticalLayout(bbox, Align.CENTER, spacing=20)

        return Pane(components, layout)

    def _info_pane(self) -> Pane:
        font = Font("roboto-bold", 26)
        colour = Ink.BLACK

        components = [
            Text(self._content.num_of_num, font, colour),
            Text(self._content.season_name, font, colour),
            Text(self._content.day, font, colour),
        ]

        bbox = BBox(top=120, left=160, bottom=HEIGHT, right=WIDTH)
        layout = VerticalLayout(bbox, Align.CENTER, spacing=10)

        return Pane(components, layout)

    def _moon_pane(self) -> Pane:
        match self._content.moon_phase:
            case MoonPhase.FULL:
                components = [
                    Circle(150, Ink.YELLOW, Ink.BLACK),
                    MoonWords(
                        self._content.moon_words[0],
                        self._content.moon_words[1],
                        Ink.BLACK
                    ),
                ]
            case MoonPhase.NEW:
                components = [
                    Circle(150, Ink.BLACK, Ink.BLACK),
                    MoonWords(
                        self._content.moon_words[0],
                        self._content.moon_words[1],
                        Ink.WHITE
                    ),
                ]
            case _:
                raise RuntimeError("Moon must be full or new")

        bbox = BBox(top=96, left=70, bottom=250, right=WIDTH // 2)
        layout = StackedLayout(bbox)

        return Pane(components, layout)

    def show(self, draw: ImageDraw) -> None:
        self._heading_pane().draw(draw)
        self._info_pane().draw(draw)
        self._moon_pane().draw(draw)


class BetweenUposathasView:
    GAP = 6
    SMALLEST_ICON = 25
    SMALL_ICON = 35
    MEDIUM_ICON = 40
    LARGE_ICON = 60
    LARGEST_ICON = 80

    def __init__(self, context: Context):
        self._content = Content(context)

    def _fifteen_day_appearance(self) -> IconCountMapping[Appearance]:
        appearances = IconCountMapping[Appearance](15)
        appearances[11, 15] = Appearance(self.SMALLEST_ICON, 5, self.GAP)
        appearances[8, 10] = Appearance(self.SMALL_ICON, 5, self.GAP)
        appearances[3, 7] = Appearance(self.MEDIUM_ICON, 8, self.GAP)
        appearances[2, 4] = Appearance(self.LARGE_ICON, 8, self.GAP)
        appearances[1] = Appearance(self.LARGEST_ICON, 8, self.GAP)
        return appearances

    def _fourteen_day_appearance(self) -> IconCountMapping[Appearance]:
        appearances = IconCountMapping[Appearance](14)
        appearances[8, 14] = Appearance(self.SMALL_ICON, 7, self.GAP)
        appearances[5, 7] = Appearance(self.MEDIUM_ICON, 7, self.GAP)
        appearances[2, 4] = Appearance(self.LARGE_ICON, 7, self.GAP)
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

    def _heading_pane(self) -> Pane:
        components = [
            Text("Next Uposatha", Font("roboto-bold", 30), Ink.BLACK),
            HorizontalLine(300, Ink.BLACK),
        ]

        bbox = BBox(top=20, left=0, bottom=95, right=WIDTH)
        layout = VerticalLayout(bbox, Align.CENTER, spacing=20)

        return Pane(components, layout)

    def _info_pane(self) -> Pane:
        components = [
            Text(self._content.date, Font("roboto-bold", 24), Ink.BLACK),
            Countdown(
                self._appearances(),
                self._content.today,
                self._content.falls_on,
                self._content.moon_phase
            ),
            Text(self._content.details, Font("roboto-bold", 24), Ink.BLACK),
        ]

        bbox = BBox(top=96, left=0, bottom=HEIGHT, right=WIDTH)
        layout = VerticalLayout(bbox, Align.CENTER, spacing=20)

        return Pane(components, layout)

    def show(self, draw: ImageDraw) -> None:
        self._heading_pane().draw(draw)
        self._info_pane().draw(draw)
