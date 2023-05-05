from PIL import ImageDraw, ImageFont

from screen import ImageConfig
from components import Rectangle, Text
from layout import ImageComponent, BoundingBox


class Countdown:
    def __init__(self, icons: list[ImageComponent], gap: int):
        if len(icons) < 1:
            raise ValueError("At least one icon is required")

        if not icons_are_square(icons):
            raise ValueError("Icons must be square")

        if not icons_are_same_size(icons):
            raise ValueError("All icons must be the same size")

        self._icons = icons
        self._icon_size = icons[0].width()
        self._gap = gap

    def height(self) -> int:
        return self._icon_size

    def width(self) -> int:
        spaces = len(self._icons) - 1
        distance = self._icon_size + self._gap
        return spaces * distance + self._icon_size

    def draw(self, x: int, y: int) -> None:
        bbox = BoundingBox(top=y, left=x, height=self.height(), width=self.width())

        layout = CountdownLayout(
            bbox=bbox,
            icons=self._icons,
            icon_size=self._icon_size,
            gap=self._gap)

        layout.draw()


XY = tuple[int, int]


class CountdownLayout:
    """ A sub-layout for countdown icons"""
    def __init__(self, bbox: BoundingBox, icons: list[ImageComponent], icon_size: int, gap: int):
        self._bbox = bbox
        self._icons = icons
        self._icon_distance = icon_size + gap
        self._offset = icon_size // 2

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


class Icons:
    def __init__(self,
                 draw: ImageDraw,
                 config: ImageConfig,
                 icon_size: int,
                 letters: list[str]):
        self._draw = draw
        self._config = config
        self._icon_size = icon_size
        self._letters = letters

    @property
    def icon_size(self) -> int:
        return self._icon_size

    @property
    def icons(self) -> list[LetterIcon]:
        return [
            LetterIcon(draw=self._draw,
                       font=self._config.font_styles.COUNTDOWN,
                       background=self._config.palette.BLACK,
                       foreground=self._config.palette.WHITE,
                       letter=letter,
                       size=self._icon_size)
            for letter in self._letters
        ]


def icons_are_square(icons: list[ImageComponent]) -> bool:
    return all([icon.height() == icon.width() for icon in icons])


def icons_are_same_size(icons: list[ImageComponent]) -> bool:
    return len({icon.width() for icon in icons}) == 1
