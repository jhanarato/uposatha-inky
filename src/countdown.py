import math
import itertools

from collections.abc import Sequence, Iterator
from datetime import date

from PIL import ImageDraw
from boltons.timeutils import daterange

from uposatha.elements import MoonPhase

from components import DayOfWeekIcon, BlankIcon, FullMoonIcon
from layout import ImageComponent
from screen import ImageConfig


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

        self._start = start
        self._end = end

        self._icons = Icons(
            draw=draw,
            config=config,
            icon_size=icon_size,
            letters=self.letters(),
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

    def letters(self) -> list[str]:
        return [date_.strftime("%a")[0]
                for date_ in daterange(self._start, self._end)]

    def draw(self, x: int, y: int) -> None:
        spacing = self._gap + self._icons.icon_size

        for icon, row, column in self._grid:
            icon.draw(
                x + (column * spacing),
                y + (row * spacing)
            )

    def __str__(self):
        return "".join([str(icon) for icon in self._icons])


class Icons(Sequence[ImageComponent]):
    """ A sequence of icons representing the days until the next uposatha """
    def __init__(self,
                 draw: ImageDraw,
                 config: ImageConfig,
                 icon_size: int,
                 letters: list[str],
                 moon_phase: MoonPhase):

        self._icon_size = icon_size
        self._icons: list[ImageComponent] = [
            DayOfWeekIcon(draw=draw,
                          font=config.font_styles.COUNTDOWN,
                          background=config.palette.BLACK,
                          foreground=config.palette.WHITE,
                          letter=letter,
                          size=icon_size)
            for letter in letters
        ]

        self._icons.append(FullMoonIcon(size=10))

    def __len__(self):
        return len(self._icons)

    def __getitem__(self, item) -> ImageComponent:
        return self._icons[item]

    @property
    def icon_size(self) -> int:
        return self._icon_size

    def __str__(self):
        return "".join(
            [str(icon) for icon in self._icons]
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
