import math
import itertools

from collections.abc import Sequence, Iterator
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Callable

from PIL import ImageDraw

from uposatha.elements import MoonPhase

from components import DayOfWeekIcon, FullMoonIcon, NewMoonIcon
from layout import ImageComponent
from screen import ImageConfig


@dataclass(frozen=True)
class Appearance:
    icon_size: int
    max_columns: int
    gap: int


Resizer = Callable[[int], Appearance]


class Countdown:
    """ An image component displaying the days of the week up to the next uposatha """
    def __init__(self, draw: ImageDraw,
                 config: ImageConfig,
                 resizer: Resizer,
                 start: date,
                 end: date,
                 moon_phase: MoonPhase,
                 ):

        self._icons = Icons(
            draw=draw,
            config=config,
            icon_size=0,
            start=start,
            end=end,
            moon_phase=moon_phase
        )

        appearance = resizer(len(self._icons))

        self._icons.icon_size = appearance.icon_size

        self._layout = GridLayout(appearance)
        self._layout.icon_count(len(self._icons))
        self._layout.gap(appearance.gap)

    def height(self) -> int:
        return self._layout.total_height

    def width(self) -> int:
        return self._layout.total_width

    def draw(self, x: int, y: int) -> None:
        self._layout.starting_coordinates(x, y)

        for icon, coordinates in zip(self._icons, self._layout.icon_coordinates()):
            icon.draw(*coordinates)

    @property
    def icon_size(self) -> int:
        return self._icons.icon_size

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

    def day_of_week_icon(self, day: date) -> ImageComponent:
        return DayOfWeekIcon(
            draw=self._draw,
            size=self.icon_size,
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
            return self.moon_icon()

        day = self._start + timedelta(item)
        return self.day_of_week_icon(day)

    def __str__(self):
        return "".join(
            [str(icon) for icon in self]
        )


class GridLayout:
    def __init__(self, appearance: Appearance):
        self._appearance = appearance
        self._icon_count = 0
        self._gap = 0
        self._start_x = 0
        self._start_y = 0

    def icon_count(self, count: int) -> None:
        self._icon_count = count

    def gap(self, gap: int) -> None:
        self._gap = gap

    def starting_coordinates(self, x: int, y: int) -> None:
        self._start_x = x
        self._start_y = y

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
        gap_height = self._gap * (self.rows - 1)
        return icon_height + gap_height

    @property
    def total_width(self) -> int:
        icon_width = self.appearance.icon_size * self.columns
        gap_width = self._gap * (self.columns - 1)
        return icon_width + gap_width

    @property
    def empty(self) -> int:
        return (self.rows * self.columns) - self._icon_count

    @property
    def spacing(self) -> int:
        return self.appearance.icon_size + self._gap

    def positions(self) -> Iterator[tuple[int, int]]:
        positions = itertools.product(
            range(self.rows),
            range(self.columns)
        )

        for _ in range(self.empty):
            next(positions)

        yield from positions

    def icon_coordinates(self) -> Iterator[tuple[int, int]]:
        for row, column in self.positions():
            x = self._start_x + (column * self.spacing)
            y = self._start_y + (row * self.spacing)
            yield x, y

def zoom_on_approach(icons: int) -> Appearance:
    if icons > 7:
        max_columns = 8
        icon_size = 30
        gap = 4
    elif icons > 3:
        # TODO We don't need to change max_columns here. It can resize itself.
        max_columns = icons
        icon_size = 40
        gap = 4
    else:
        # TODO: As above.
        max_columns = icons
        icon_size = 50
        gap = 4

    return Appearance(icon_size=icon_size, max_columns=max_columns, gap=gap)
