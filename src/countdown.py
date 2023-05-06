from collections.abc import Sequence
from typing import Any

from icons import CountdownIcons
from layout import ImageComponent, BoundingBox


class Countdown:
    """ An image component displaying the days of the week up to the next uposatha """
    def __init__(self, icons: CountdownIcons, gap: int):
        self._icons = icons
        self._gap = gap

    def height(self) -> int:
        return self._icons.icon_size

    def width(self) -> int:
        spaces = len(self._icons) - 1
        distance = self._icons.icon_size + self._gap
        return spaces * distance + self._icons.icon_size

    def draw(self, x: int, y: int) -> None:
        bbox = BoundingBox(top=y, left=x, height=self.height(), width=self.width())

        layout = CountdownLayout(
            bbox=bbox,
            icons=self._icons,
            gap=self._gap)

        layout.draw()

def seq_to_rows(seq: Sequence, row_length: int) -> list[list[Any]]:
    first_row = seq[0:2]
    second_row = seq[2:4]
    return [first_row, second_row]

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
