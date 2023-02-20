import pytest
from datetime import date, timedelta
from content import countdown_letters, split_countdown

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
    "days_left,split",
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
def test_split(days_left, split):
    end = date(2011, 2, 3) # 15 day new moon.
    start = end - timedelta(days_left)
    letters = countdown_letters(start, end)
    assert split_countdown(letters) == split
