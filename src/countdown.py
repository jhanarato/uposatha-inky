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
        self._spacing = self._icon_size + self._gap

    def height(self) -> int:
        return self._icon_size

    def width(self) -> int:
        spaces = len(self._icons) - 1
        return spaces * self._spacing + self._icon_size

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


def icons_are_square(icons: list[ImageComponent]) -> bool:
    return all([icon.height() == icon.width() for icon in icons])


def icons_are_same_size(icons: list[ImageComponent]) -> bool:
    return len({icon.width() for icon in icons}) == 1




def max_width(components: list[ImageComponent]) -> int:
    return max(components, key=lambda component: component.width()).width()


def max_height(components: list[ImageComponent]) -> int:
    return max(components, key=lambda component: component.height()).height()
