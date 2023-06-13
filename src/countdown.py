import math
import itertools

from collections.abc import Sequence, Iterator
from dataclasses import dataclass
from datetime import date, timedelta

from PIL import ImageDraw
from boltons.timeutils import daterange

from uposatha.elements import MoonPhase

from components import DayOfWeekIcon, BlankIcon, FullMoonIcon, NewMoonIcon
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

        self._gap = gap
        self._grid = Grid(self._icons, max_columns)

    def height(self) -> int:
        icon_height = self._icons.icon_size * self._grid.rows
        gap_height = self._gap * (self._grid.rows - 1)
        return icon_height + gap_height

    def width(self) -> int:
        icon_width = self._icons.icon_size * self._grid.columns
        gap_height = self._gap * (self._grid.columns - 1)
        return icon_width + gap_height

    def draw(self, x: int, y: int) -> None:
        for icon, row, column in self._grid:
            xy = icon_xy(x, y, row, column, self._gap, self._icons.icon_size)
            icon.draw(*xy)

    def __str__(self):
        return "".join([str(icon) for icon in self._icons])


def icon_xy(parent_x: int, parent_y: int,
            row: int, column: int,
            gap: int, icon_size: int) -> tuple[int, int]:
    spacing = gap + icon_size
    icon_x = parent_x + (column * spacing)
    icon_y = parent_y + (row * spacing)
    return icon_x, icon_y


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


class Grid:
    """ An iterable of icons in grid positions """
    def __init__(self, icons: Icons, max_columns: int):
        self._icons = icons
        self._max_columns = max_columns

    def has_single_row(self) -> bool:
        return len(self._icons) <= self._max_columns

    @property
    def columns(self) -> int:
        if self.has_single_row():
            return len(self._icons)
        return self._max_columns

    @property
    def rows(self) -> int:
        return math.ceil(len(self._icons) / self._max_columns)

    def _blanks(self) -> list[BlankIcon]:
        empty = (self.rows * self.columns) - len(self._icons)
        return [BlankIcon(size=self._icons.icon_size)
                for _ in range(empty)]

    def __iter__(self) -> Iterator[tuple[ImageComponent, int, int]]:
        icons = itertools.chain(self._blanks(), self._icons)
        positions = itertools.product(range(self.rows), range(self.columns))

        for icon, position in zip(icons, positions, strict=True):
            yield icon, position[0], position[1]

    def __str__(self):
        return "".join([str(pos[0]) for pos in self])


class IconPositions:
    def __init__(self, icon_count: int, max_columns: int):
        self._icon_count = icon_count
        self._max_columns = max_columns

    @property
    def rows(self) -> int:
        return math.ceil(self._icon_count / self._max_columns)

    def __iter__(self) -> Iterator[tuple[int, int]]:
        yield 0, 0
