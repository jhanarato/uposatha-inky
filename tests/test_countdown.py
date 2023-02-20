from datetime import date, timedelta
from content import countdown

def test_countdown_fourteen():
    a_friday = date(2010, 3, 26)
    uposatha = a_friday + timedelta(14)
    expected = ["F", "S", "S", "M", "T", "W", "T", "F",
                "S", "S", "M", "T", "W", "T", "F"]
    assert countdown(a_friday, uposatha) == expected

def test_countdown_day_before():
    a_friday = date(2010, 3, 26)
    uposatha = date(2010, 3, 27)
    assert countdown(a_friday, uposatha) == ["F", "S"]

def test_countdown_on_day():
    a_friday = date(2010, 3, 26)
    uposatha = a_friday
    assert countdown(a_friday, uposatha) == ["F"]