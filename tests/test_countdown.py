import pytest
from datetime import date, timedelta
from content import countdown_letters
from images import centre_points
from components import Countdown
from layout import ImageComponent, Layout, ArrangedComponent, Align


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

class LetterDummy:
    def __init__(self):
        pass

    def height(self) -> int:
        return 0

    def width(self) -> int:
        return 0

    def draw(self, x: int, y: int) -> None:
        pass


class LetterSpy:
    def __init__(self, size: int):
        self.size = int
        self.last_draw_at = None

    def height(self) -> int:
        return 10

    def width(self) -> int:
        return 10

    def draw(self, x: int, y: int) -> None:
        self.last_draw_at = (x, y)


def test_should_create_component():
    letters = [LetterDummy()]
    component = Countdown(letters)

def test_should_draw_letter():
    letters = [LetterDummy()]
    component = Countdown(letters)
    component.draw(0, 0)

def test_should_position_single_letter_at_centre():
    letters = [LetterSpy(size=10)]
    component = Countdown(letters)
    layout = Layout(100, 100)
    layout.add(
        ArrangedComponent(
            component=component,
            align=Align.CENTRE,
            space_before=0,
            space_after=0
        )
    )
    layout.draw()

    assert letters[0].last_draw_at == (45, 0)

def test_should_set_width_of_countdown_for_one_letter():
    letters = [LetterSpy(size=10)]
    component = Countdown(letters)
    assert component.width() == 10

def test_should_set_width_for_three_letters():
    letters = [
        LetterSpy(size=8),
        LetterSpy(size=8),
        LetterSpy(size=8),
    ]

    component = Countdown(letters)
    assert component.width() == 30
