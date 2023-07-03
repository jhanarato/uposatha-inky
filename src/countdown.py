import math
import itertools

from collections.abc import Sequence, Iterator
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Callable, Optional

from PIL import ImageDraw

from uposatha.elements import MoonPhase

from components import DayOfWeekIcon, FullMoonIcon, NewMoonIcon
from layout import ImageComponent
from screen import ImageConfig

GAP = 4
SMALLEST_ICON = 25
SMALL_ICON = 35
MEDIUM_ICON = 40
LARGE_ICON = 45
LARGEST_ICON = 80

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


class AppearanceForIconCount:
    def __init__(self, max_icons: int) -> None:
        self._max_icons = max_icons
        self._appearances_dict: dict[int, Appearance] = {}

    def __setitem__(self, key: tuple[int, int] | int, value: Appearance):
        for key in self._key_range(key):
            self._check_bounds(key)
            self._appearances_dict[key] = value

    def __getitem__(self, item: int) -> Appearance:
        self._check_bounds(item)
        return self._appearances_dict[item]

    def __delitem__(self, key):
        del(self._appearances_dict[key])

    def _key_range(self, key) -> list[int]:
        if isinstance(key, int):
            keys = [key]
        else:
            keys = list(range(key[0], key[1] + 1))
        return keys

    def _check_bounds(self, item):
        if item < 1:
            raise KeyError("Number of icons is always positive")
        if item > self._max_icons:
            raise KeyError("Index greater than maximum number of icons")

    def __iter__(self):
        return iter(self._appearances_dict)

    def __len__(self) -> int:
        return self._max_icons


def zoom_on_approach(icons: int, fourteen_day: bool) -> Appearance:
    if fourteen_day:
        appearances = AppearanceForIconCount(14)
        appearances[8, 14] = Appearance(SMALL_ICON, 7, GAP)
        appearances[4, 7] = Appearance(MEDIUM_ICON, 7, GAP)
        appearances[2, 3] = Appearance(LARGE_ICON, 7, GAP)
        appearances[1] = Appearance(LARGEST_ICON, 7, GAP)
    else:
        appearances = AppearanceForIconCount(15)
        appearances[11, 15] = Appearance(SMALLEST_ICON, 5, GAP)
        appearances[8, 10] = Appearance(SMALL_ICON, 8, GAP)
        appearances[4, 7] = Appearance(MEDIUM_ICON, 8, GAP)
        appearances[2, 3] = Appearance(LARGE_ICON, 8, GAP)
        appearances[1] = Appearance(LARGEST_ICON, 8, GAP)

    return appearances[icons]
