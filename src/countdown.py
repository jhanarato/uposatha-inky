from PIL import ImageDraw, ImageFont

from screen import ImageConfig
from components import Rectangle, Text
from layout import ImageComponent, BoundingBox


class LetterIcon:
    def __init__(self,
                 draw: ImageDraw,
                 font: ImageFont,
                 background: int,
                 foreground: int,
                 letter: str,
                 size: int) -> None:
        self._size = size
        self._rect = Rectangle(draw, self.height(), self.width(), background)
        self._text = Text(draw, letter, font, foreground)

    def height(self) -> int:
        return self._size

    def width(self) -> int:
        return self._size

    def _text_x(self, component_x: int) -> int:
        return component_x + (self.width() - self._text.width()) // 2

    def _text_y(self, component_y: int) -> int:
        return component_y + (self.height() - self._text.height()) // 2

    def draw(self, x: int, y: int) -> None:
        self._rect.draw(x, y)
        self._text.draw(self._text_x(x), self._text_y(y))


def create_icons(draw: ImageDraw,
                 config: ImageConfig,
                 size: int,
                 letters: list[str]) -> list[LetterIcon]:
    return [
        LetterIcon(draw=draw,
                   font=config.font_styles.COUNTDOWN,
                   background=config.palette.BLACK,
                   foreground=config.palette.WHITE,
                   letter=letter,
                   size=size)
        for letter in letters
    ]


class Countdown:
    def __init__(self, icons: list[ImageComponent], gap: int):
        self._check_icons(icons)
        self._icons = icons
        self._gap = gap
        self._icon_width = max_width(self._icons)
        self._icon_height = max_height(self._icons)

    def _check_icons(self, icons: list[ImageComponent]) -> None:
        if len(icons) < 1:
            raise ValueError("At least one icon is required")

        for icon in icons:
            if icon.height() != icon.width():
                raise ValueError("Icons must be square")

    def _horizontal_spacing(self) -> int:
        return self._icon_width + self._gap

    def _vertical_spacing(self) -> int:
        return self._icon_height + self._gap

    def height(self) -> int:
        return self._icon_height

    def width(self) -> int:
        spaces = len(self._icons) - 1
        return spaces * self._horizontal_spacing() + self._icon_width

    def draw(self, x: int, y: int) -> None:
        bbox = BoundingBox(top=y, left=x, height=self.height(), width=self.width())
        layout = CountdownLayout(bbox=bbox, icons=self._icons, gap=self._gap)
        layout.draw()


XY = tuple[int, int]


class CountdownLayout:
    """ A sub-layout for countdown icons"""
    def __init__(self, bbox: BoundingBox, icons: list[ImageComponent], gap: int = 0):
        self._bbox = bbox
        self._icons = icons
        self._gap = gap
        self._offset = self._spacing() // 2
        self._x_start = self._bbox.left + self._offset
        self._y_start = self._bbox.top + self._offset

    def _spacing(self) -> int:
        return max_width(self._icons) + self._gap

    def _centers(self) -> list[XY]:
        return [(self._x_start + self._spacing() * icon_number, self._y_start)
                for icon_number in range(len(self._icons))]

    def _to_xy(self, centers: list[XY]) -> list[XY]:
        return [(cx - self._offset, cy - self._offset)
                for cx, cy in centers]

    def draw(self):
        icons_centers = self._centers()
        icons_xy = self._to_xy(icons_centers)
        for icon, xy in zip(self._icons, icons_xy):
            icon.draw(*xy)


def max_width(components: list[ImageComponent]) -> int:
    if not components:
        return 0

    return max(components, key=lambda component: component.width()).width()


def max_height(components: list[ImageComponent]) -> int:
    if not components:
        return 0

    return max(components, key=lambda component: component.height()).height()
