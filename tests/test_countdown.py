import pytest
from datetime import date, timedelta
from itertools import islice
from content import countdown_letters, split_countdown
from images import letter_coords, CountdownArea, centre_points


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
    "days_left,countdown",
    [
        (14, (["T", "F", "S", "S", "M", "T", "W"],
              ["T", "F", "S", "S", "M", "T", "W", "T"])),

        (8, (["W"], ["T", "F", "S", "S", "M", "T", "W", "T"])),
        (7, ([], ["T", "F", "S", "S", "M", "T", "W", "T"])),
        (6, ([], ["F", "S", "S", "M", "T", "W", "T"])),
        (1, ([], ["W", "T"])),
        (0, ([], ["T"])) # The uposatha
    ]
)
def test_split(days_left, countdown):
    end = date(2011, 2, 3) # 15 day new moon.
    start = end - timedelta(days_left)
    letters = countdown_letters(start, end)
    actual = split_countdown(letters)
    assert actual.top_row == countdown[0]
    assert actual.bottom_row == countdown[1]

@pytest.fixture
def countdown_area():
    return CountdownArea(
        x=30,
        y=50,
        width=240,
        height=100,
        border=10,
        letter_spacing=20,
        row_spacing=20
    )


@pytest.mark.parametrize(
    "letter_num,row_num,x",
    [
        (0, 0, 260),
        (1, 0, 240),
        (1, 1, 240),
        (2, 0, 220)
    ]
)
def test_countdown_letter_x(countdown_area, letter_num, row_num, x):
    assert letter_coords(countdown_area, letter_num, row_num)[0] == x


@pytest.mark.parametrize(
    "letter_num,row_num,y",
    [
        (0, 0, 50),
        (1, 0, 50),
        (0, 1, 70)
    ]
)
def test_countdown_letter_y(countdown_area, letter_num, row_num, y):
    assert letter_coords(countdown_area, letter_num, row_num)[1] == y

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
