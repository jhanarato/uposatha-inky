import math
import itertools

from collections.abc import Sequence, Iterator
from dataclasses import dataclass
from datetime import date, timedelta
from enum import Enum, auto
from typing import Callable

from PIL import ImageDraw

from uposatha.elements import MoonPhase

from components import DayOfWeekIcon, FullMoonIcon, NewMoonIcon
from layout import ImageComponent
from screen import ImageConfig

GAP = 4
SMALLEST_ICON = 0
SMALL_ICON = 35
MEDIUM_ICON = 40
LARGE_ICON = 45

@dataclass(frozen=True)
class Appearance:
    icon_size: int
    max_columns: int
    gap: int


Resizer = Callable[[int, bool], Appearance]


class Countdown:
    """ An image component displaying the days of the week up to the next uposatha """
    def __init__(self, draw: ImageDraw, config: ImageConfig, resizer: Resizer,
                 start: date, end: date, moon_phase: MoonPhase, fourteen_day: bool):

        self._icons = Icons(
            draw=draw,
            config=config,
            icon_size=0,
            start=start,
            end=end,
            moon_phase=moon_phase
        )

        appearance = resizer(len(self._icons), fourteen_day)
        self._icons.icon_size = appearance.icon_size
        self._layout = GridLayout(appearance, len(self._icons))

    def height(self) -> int:
        return self._layout.total_height

    def width(self) -> int:
        return self._layout.total_width

    def draw(self, x: int, y: int) -> None:
        drawable = zip(
            self._icons,
            self._layout.icon_coordinates(start_x=x, start_y=y)
        )

        for icon, coordinates in drawable:
            icon.draw(*coordinates)

    def __str__(self):
        return "".join([str(icon) for icon in self._icons])


class Icons(Sequence[ImageComponent]):
    """ A sequence of icons representing the days until the next uposatha """
    def __init__(self,
                 draw: ImageDraw,
                 config: ImageConfig,
                 icon_size: int,
                 start: date,
                 end: date,
                 moon_phase: MoonPhase):

        self.icon_size = icon_size
        self._draw = draw
        self._config = config
        self._start = start
        self._end = end
        self._moon_phase = moon_phase

    def _day_of_week_icon(self, day: date) -> ImageComponent:
        return DayOfWeekIcon(
            draw=self._draw,
            size=self.icon_size,
            font=self._config.font_styles.COUNTDOWN,
            background=self._config.palette.BLACK,
            foreground=self._config.palette.WHITE,
            letter=day.strftime("%a")[0]
        )

    def _moon_icon(self) -> ImageComponent:
        match self._moon_phase:
            case MoonPhase.FULL:
                return FullMoonIcon(
                    draw=self._draw,
                    fill=self._config.palette.YELLOW,
                    outline=self._config.palette.BLACK,
                    size=self.icon_size)

            case MoonPhase.NEW:
                return NewMoonIcon(
                   draw=self._draw,
                   fill=self._config.palette.BLACK,
                   size=self.icon_size)

            case MoonPhase.WANING | MoonPhase.WAXING:
                raise RuntimeError("Moon phase must be full or new")

    def __len__(self):
        return (self._end - self._start).days + 1

    def __getitem__(self, item) -> ImageComponent:
        if item < 0:
            raise IndexError("No negative indexes")
        if item >= len(self):
            raise IndexError("No such icon")

        if item == len(self) - 1:
            return self._moon_icon()

        day = self._start + timedelta(item)
        return self._day_of_week_icon(day)

    def __str__(self):
        return "".join(
            [str(icon) for icon in self]
        )


class GridLayout:
    def __init__(self, appearance: Appearance, icon_count: int):
        self._appearance = appearance
        self._icon_count = icon_count

    @property
    def appearance(self) -> Appearance:
        return self._appearance

    @property
    def rows(self) -> int:
        return math.ceil(self._icon_count / self.appearance.max_columns)

    @property
    def columns(self) -> int:
        if self._icon_count < self.appearance.max_columns:
            return self._icon_count
        return self.appearance.max_columns

    @property
    def total_height(self) -> int:
        icon_height = self.appearance.icon_size * self.rows
        gap_height = self.appearance.gap * (self.rows - 1)
        return icon_height + gap_height

    @property
    def total_width(self) -> int:
        icon_width = self.appearance.icon_size * self.columns
        gap_width = self.appearance.gap * (self.columns - 1)
        return icon_width + gap_width

    @property
    def empty(self) -> int:
        return (self.rows * self.columns) - self._icon_count

    @property
    def spacing(self) -> int:
        return self.appearance.icon_size + self.appearance.gap

    def positions(self) -> Iterator[tuple[int, int]]:
        positions = itertools.product(
            range(self.rows),
            range(self.columns)
        )

        for _ in range(self.empty):
            next(positions)

        yield from positions

    def icon_coordinates(self, start_x: int, start_y: int) -> Iterator[tuple[int, int]]:
        for row, column in self.positions():
            x = start_x + (column * self.spacing)
            y = start_y + (row * self.spacing)
            yield x, y

def zoom_on_approach(icons: int, fourteen_day: bool) -> Appearance:
    if fourteen_day:
        max_columns = 7
    else:
        max_columns = 8

    if icons < 4:
        icon_size = LARGE_ICON
    elif icons < max_columns:
        icon_size = MEDIUM_ICON
    else:
        icon_size = SMALL_ICON

    return Appearance(icon_size=icon_size, max_columns=max_columns, gap=GAP)

class ColumnMode(Enum):
    THREE_ROW = auto()
    TWO_ROW_15_DAY = auto()
    TWO_ROW_14_DAY = auto()
    ONE_ROW_LONGER = auto()
    ONE_ROW_SHORTER = auto()

def column_mode(icons: int, fourteen_day: bool) -> ColumnMode:
    return ColumnMode.THREE_ROW
