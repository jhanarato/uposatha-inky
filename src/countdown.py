import math
import itertools

from collections.abc import Sequence, Iterator, Iterable
from dataclasses import dataclass
from datetime import date, timedelta

from PIL import ImageDraw

from uposatha.elements import MoonPhase

from components import DayOfWeekIcon, FullMoonIcon, NewMoonIcon
from layout import ImageComponent
from screen import ImageConfig

@dataclass
class Appearance:
    icon_size: int
    max_columns: int
    gap: int


def appearance(today: date, uposatha: date) -> Appearance:
    days_inclusive = (uposatha - today).days + 1

    small = Appearance(max_columns=8, icon_size=30, gap=4)
    medium = Appearance(max_columns=days_inclusive, icon_size=40, gap=4)
    large = Appearance(max_columns=days_inclusive, icon_size=50, gap=4)

    if days_inclusive > 7:
        return small
    if days_inclusive > 3:
        return medium
    else:
        return large


class Countdown:
    """ An image component displaying the days of the week up to the next uposatha """
    def __init__(self, draw: ImageDraw,
                 config: ImageConfig,
                 start: date,
                 end: date,
                 moon_phase: MoonPhase,
                 icon_size: int,
                 gap: int,
                 max_columns: int
                 ):

        self._icons = Icons(
            draw=draw,
            config=config,
            icon_size=icon_size,
            start=start,
            end=end,
            moon_phase=moon_phase
        )

        self._layout = GridLayout()
        self._layout.icon_count(len(self._icons))
        self._layout.icon_size(icon_size)
        self._layout.gap(gap)
        self._layout.max_columns(max_columns)

    def height(self) -> int:
        return self._layout.total_height

    def width(self) -> int:
        return self._layout.total_width

    def draw(self, x: int, y: int) -> None:
        self._layout.start_at(x, y)

        for position, icon in zip(self._layout.icon_positions(), self._icons):
            icon.draw(*position)

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

        self._draw = draw
        self._config = config
        self._start = start
        self._end = end
        self._moon_phase = moon_phase
        self._icon_size = icon_size

    def day_of_week_icon(self, day: date) -> ImageComponent:
        return DayOfWeekIcon(
            draw=self._draw,
            size=self._icon_size,
            font=self._config.font_styles.COUNTDOWN,
            background=self._config.palette.BLACK,
            foreground=self._config.palette.WHITE,
            letter=day.strftime("%a")[0]
        )

    def moon_icon(self) -> ImageComponent:
        match self._moon_phase:
            case MoonPhase.FULL:
                return FullMoonIcon(
                    draw=self._draw,
                    fill=self._config.palette.YELLOW,
                    outline=self._config.palette.BLACK,
                    size=self._icon_size)

            case MoonPhase.NEW:
                return NewMoonIcon(
                   draw=self._draw,
                   fill=self._config.palette.BLACK,
                   size=self._icon_size)

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
            return self.moon_icon()

        day = self._start + timedelta(item)
        return self.day_of_week_icon(day)

    @property
    def icon_size(self) -> int:
        return self._icon_size

    def __str__(self):
        return "".join(
            [str(icon) for icon in self]
        )


class GridLayout:
    def __init__(self):
        self._max_columns = 0
        self._icon_count = 0
        self._icon_size = 0
        self._gap = 0
        self._start_x = 0
        self._start_y = 0

    def max_columns(self, columns: int) -> None:
        self._max_columns = columns

    def icon_count(self, count: int) -> None:
        self._icon_count = count

    def icon_size(self, size: int) -> None:
        self._icon_size = size

    def gap(self, gap: int) -> None:
        self._gap = gap

    def start_at(self, x: int, y: int) -> None:
        self._start_x = x
        self._start_y = y

    @property
    def rows(self) -> int:
        return math.ceil(self._icon_count / self._max_columns)

    @property
    def columns(self) -> int:
        if self._icon_count < self._max_columns:
            return self._icon_count
        return self._max_columns

    @property
    def total_height(self) -> int:
        icon_height = self._icon_size * self.rows
        gap_height = self._gap * (self.rows - 1)
        return icon_height + gap_height

    @property
    def total_width(self) -> int:
        icon_width = self._icon_size * self.columns
        gap_width = self._gap * (self.columns - 1)
        return icon_width + gap_width

    @property
    def empty(self) -> int:
        return (self.rows * self.columns) - self._icon_count

    @property
    def spacing(self) -> int:
        return self._icon_size + self._gap

    def positions(self) -> Iterator[tuple[int, int]]:
        positions = itertools.product(
            range(self.rows),
            range(self.columns)
        )

        for _ in range(self.empty):
            next(positions)

        yield from positions

    def icon_positions(self) -> Iterator[tuple[int, int]]:
        for row, column in self.positions():
            x = (column * self.spacing) + self._start_x
            y = (row * self.spacing) + self._start_y
            yield x, y