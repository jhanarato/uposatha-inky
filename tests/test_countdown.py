from datetime import date, timedelta
from typing import Optional

import pytest

from content import countdown_letters
from images import centre_points
from components import LetterIcon
from layout import Layout, ArrangedComponent, Align, BoundingBox, CountdownLayout


def test_letters_fifteen():
    a_friday = date(2010, 3, 26)
    uposatha = a_friday + timedelta(14)
    expected = ["F", "S", "S", "M", "T", "W", "T",
                "F", "S", "S", "M", "T", "W", "T", "F"]
    assert countdown_letters(a_friday, uposatha) == expected

def test_letters_day_before():
    a_friday = date(2010, 3, 26)
    uposatha = date(2010, 3, 27)
    assert countdown_letters(a_friday, uposatha) == ["F", "S"]

def test_letters_on_day():
    a_friday = date(2010, 3, 26)
    uposatha = a_friday
    assert countdown_letters(a_friday, uposatha) == ["F"]

@pytest.mark.parametrize(
    "y_coord,width,spacing,number,result",
    [
        (100, 400, 20, 1, [(200, 100)]),
        (100, 400, 20, 2, [(190, 100), (210, 100)]),
        (100, 400, 20, 3, [(180, 100), (200, 100), (220, 100)]),
    ]
)
def test_centre_points(y_coord, width, spacing, number, result):
    assert centre_points(y_coord=y_coord,
                         screen_width=width,
                         spacing=spacing,
                         number_of_points=number) == result


class LetterSpy:
    def __init__(self, size: int):
        self._size = size
        self.last_draw_at = None

    def height(self) -> int:
        return self._size

    def width(self) -> int:
        return self._size

    def draw(self, x: int, y: int) -> None:
        self.last_draw_at = (x, y)

    def center(self) -> Optional[tuple[int, int]]:
        if self.last_draw_at is None:
            return None

        x, y = self.last_draw_at
        center_x = x + int(self.width() / 2)
        center_y = y + int(self.height() / 2)
        return center_x, center_y


def test_should_set_width_of_countdown_for_one_letter(one_day_countdown):
    assert one_day_countdown.width() == 10


def test_should_set_width_for_three_letters(three_day_countdown):
    assert three_day_countdown.width() == 30


def test_should_set_countdown_height_to_icon_height(one_day_countdown):
    assert one_day_countdown.height() == 10


def test_should_set_icon_dimensions():
    icon = LetterIcon(letter="M", size=10)
    assert icon.height() == 10
    assert icon.width() == 10

def test_should_assign_a_letter_to_an_icon():
    letters = ["M", "T", "W"]
    icons = [LetterIcon(letter, 10) for letter in letters]
    assert icons[0]._letter == "M"
    assert icons[1]._letter == "T"
    assert icons[2]._letter == "W"


def test_should_position_single_letter_at_centre(one_day_countdown):
    layout = Layout(100, 100)
    layout.add(
        ArrangedComponent(
            component=one_day_countdown,
            align=Align.CENTRE,
            space_before=0,
            space_after=0
        )
    )
    layout.draw()

    assert one_day_countdown._icons[0].last_draw_at == (45, 0)


def test_should_layout_single_icon():
    icons = [LetterSpy(size=10)]
    box = BoundingBox(top=0, left=0, height=100, width=100)
    layout = CountdownLayout(box=box, icons=icons)
    layout.draw()
    assert icons[0].last_draw_at
