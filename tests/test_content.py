from datetime import date

from content import (
    next_uposatha_content, NextUposathaContent
)

def test_next_uposatha_day():
    today = date(2023, 2, 13)
    actual = next_uposatha_content(today)
    expected = NextUposathaContent(
        day="Sunday",
        date="19/02/23",
        days_until="In 6 days"
    )

    assert actual == expected
