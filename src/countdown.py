import math
import itertools

from collections.abc import Sequence, Iterator, MutableMapping
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Callable, TypeVar

from PIL import ImageDraw

from uposatha.elements import MoonPhase

from components import DayOfWeekIcon, FullMoonIcon, NewMoonIcon, Drawable
from screen import ImageConfig

@dataclass(frozen=True)
class Appearance:
    icon_size: int
    max_columns: int
    gap: int


Resizer = Callable[[int, bool], Appearance]

T = TypeVar("T")

class IconCountMapping(MutableMapping[T]):
    """ Map a type to the number of icons being displayed.
        The key is bounds-checked to be between 1 and the
        maximum number of icons that can be displayed.
        Keys can be provided individually, or as a range.
    """
    def __init__(self, max_icons: int) -> None:
        self._max_icons = max_icons
        self._mapping: dict[int, T] = {}

    def __setitem__(self, key: tuple[int, int] | int, value: T):
        for key in self._key_range(key):
            self._check_bounds(key)
            self._mapping[key] = value

    def __getitem__(self, item: int) -> T:
        self._check_bounds(item)
        return self._mapping.get(item)

    def __delitem__(self, key):
        del(self._mapping[key])

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
        for i in range(1, self._max_icons + 1):
            yield self._mapping.get(i)

    def __len__(self) -> int:
        return self._max_icons


class Countdown:
    """ An image component displaying the days of the week up to the next uposatha """
    def __init__(self, appearances: IconCountMapping[Appearance], start: date, end: date, moon_phase: MoonPhase):

        self._icons = Icons(
            config=ImageConfig(),
            icon_size=0,
            start=start,
            end=end,
            moon_phase=moon_phase
        )

        appearance = appearances[len(self._icons)]
        self._icons.icon_size = appearance.icon_size
        self._layout = GridLayout(appearance, len(self._icons))

    def height(self) -> int:
        return self._layout.total_height

    def width(self) -> int:
        return self._layout.total_width

    def draw(self, draw: ImageDraw, x: int, y: int) -> None:
        drawable = zip(
            self._icons,
            self._layout.coordinates(start_x=x, start_y=y)
        )

        for icon, coordinates in drawable:
            icon.draw(draw, *coordinates)

    def __str__(self):
        return "".join([str(icon) for icon in self._icons])


class Icons(Sequence[Drawable]):
    """ A sequence of icons representing the days until the next uposatha """
    def __init__(self,
                 config: ImageConfig,
                 icon_size: int,
                 start: date,
                 end: date,
                 moon_phase: MoonPhase):

        self.icon_size = icon_size
        self._config = config
        self._start = start
        self._end = end
        self._moon_phase = moon_phase

    def _day_of_week_icon(self, day: date) -> Drawable:
        return DayOfWeekIcon(
            size=self.icon_size,
            font=self._config.font_styles.COUNTDOWN,
            background=self._config.palette.BLACK,
            foreground=self._config.palette.WHITE,
            letter=day.strftime("%a")[0]
        )

    def _moon_icon(self) -> Drawable:
        match self._moon_phase:
            case MoonPhase.FULL:
                return FullMoonIcon(
                    fill=self._config.palette.YELLOW,
                    outline=self._config.palette.BLACK,
                    size=self.icon_size)

            case MoonPhase.NEW:
                return NewMoonIcon(
                   fill=self._config.palette.BLACK,
                   size=self.icon_size)

            case MoonPhase.WANING | MoonPhase.WAXING:
                raise RuntimeError("Moon phase must be full or new")

    def __len__(self):
        return (self._end - self._start).days + 1

    def __getitem__(self, item) -> Drawable:
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

    def coordinates(self, start_x: int, start_y: int) -> Iterator[tuple[int, int]]:
        for row, column in self.positions():
            x = start_x + (column * self.spacing)
            y = start_y + (row * self.spacing)
            yield x, y
