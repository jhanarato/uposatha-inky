from collections.abc import Sequence, Iterator
from dataclasses import dataclass
from typing import TypeVar

import math
from itertools import product

from icons import CountdownIcons
from layout import ImageComponent, BoundingBox


class Countdown:
    """ An image component displaying the days of the week up to the next uposatha """
    def __init__(self, icons: CountdownIcons, max_columns: int, gap: int):
        self._icons = icons
        self._gap = gap
        self._grid = IconGrid(icons, max_columns)

    def height(self) -> int:
        icon_height = self._icons.icon_size * self._grid.rows
        gap_height = self._gap * (self._grid.rows - 1)
        return icon_height + gap_height

    def width(self) -> int:
        icon_width = self._icons.icon_size * self._grid.columns
        gap_height = self._gap * (self._grid.columns - 1)
        return icon_width + gap_height

    def _draw_icon(self, icon: ImageComponent, top: int, left: int, row: int, column: int) -> None:
        spacing = self._gap + self._icons.icon_size
        x = left + column * spacing
        y = top + row * spacing
        icon.draw(x, y)

    def draw(self, x: int, y: int) -> None:
        for position in self._grid:
            self._draw_icon(position.icon, top=y, left=x, row=position.row, column=position.column)


@dataclass
class GridPosition:
    icon: ImageComponent
    row: int
    column: int


class IconGrid:
    def __init__(self, icons: Sequence[ImageComponent], max_columns: int):
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

    def __iter__(self) -> Iterator[GridPosition]:
        positions = product(range(self.rows), range(self.columns))
        skip_n(positions, (self.rows * self.columns) - len(self._icons))

        for position in zip(self._icons, positions, strict=True):
            row, col = position[1]
            yield GridPosition(position[0], row, col)

def skip_n(i: Iterator, n: int):
    [next(i) for _ in range(n)]
