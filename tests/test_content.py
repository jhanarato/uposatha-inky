from datetime import date

import pytest

from content import next_uposatha_content


@pytest.mark.parametrize(
    "today,is_fourteen_day",
    [
        (date(2011, 1, 3), True),
        (date(2011, 1, 4), True),
        (date(2011, 1, 5), False),
    ]
)
def test_should_flag_fourteen_day(today, is_fourteen_day):
    assert next_uposatha_content(today=today).fourteen_day == is_fourteen_day
