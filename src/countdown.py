from dataclasses import dataclass

import math

from itertools import repeat, chain
from collections.abc import Sequence, Iterator
from typing import TypeVar

from icons import CountdownIcons
from layout import ImageComponent, BoundingBox


class Countdown:
    """ An image component displaying the days of the week up to the next uposatha """
    def __init__(self, icons: CountdownIcons, row_length: int, gap: int):
        self._icons = icons
        self._gap = gap
        self._rows = seq_to_rows(icons, row_length)

    @property
    def rows(self):
        return len(self._rows)

    @property
    def columns(self):
        longest_row = max(self._rows, key=lambda x: len(x))
        return len(longest_row)

    def height(self) -> int:
        gaps = self.rows - 1
        return (self.rows * self._icons.icon_size) + (gaps * self._gap)

    def width(self) -> int:
        gaps = self.columns - 1
        return (self.columns * self._icons.icon_size) + (gaps * self._gap)

    def draw(self, x: int, y: int) -> None:
        bbox = BoundingBox(top=y, left=x, height=self.height(), width=self.width())

        layout = CountdownLayout(
            bbox=bbox,
            icons=self._icons,
            gap=self._gap)

        layout.draw()

T = TypeVar('T')

def seq_to_rows(seq: Sequence[T], row_length: int) -> list[list[T]]:
    full_rows, items_left_over = divmod(len(seq), row_length)

    rows = []

    if items_left_over > 0:
        rows.append(list(seq[:items_left_over]))

    for row_num in range(full_rows):
        start = items_left_over + row_num * row_length
        stop = start + row_length
        rows.append(list(seq[start:stop]))

    return rows

XY = tuple[int, int]


class CountdownLayout:
    """ A sub-layout for countdown icons. Likely to be removed soon. """
    def __init__(self, bbox: BoundingBox, icons: CountdownIcons, gap: int):
        self._bbox = bbox
        self._icons = icons
        self._icon_distance = icons.icon_size + gap
        self._offset = icons.icon_size // 2

        self._x_start = self._bbox.left + self._offset
        self._y_start = self._bbox.top + self._offset

    def _centers(self) -> list[XY]:
        return distribute_centers(
            x_start=self._x_start,
            y_start=self._y_start,
            distance=self._icon_distance,
            number_of_icons=len(self._icons)
        )

    def _to_xy(self, centers: list[XY]) -> list[XY]:
        return [(cx - self._offset, cy - self._offset)
                for cx, cy in centers]

    def draw(self):
        icons_centers = self._centers()
        icons_xy = self._to_xy(icons_centers)
        for icon, xy in zip(self._icons, icons_xy):
            icon.draw(*xy)


def distribute_centers(x_start: int, y_start: int, distance: int, number_of_icons: int) -> list[XY]:
    return [
        (x_start + distance * number, y_start)
        for number in range(number_of_icons)
    ]

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
        yield GridPosition(
            icon=self._icons[0],
            row=0,
            column=2
        )
