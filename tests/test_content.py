from datetime import date

import pytest
from uposatha.calendar import Calendar
from uposatha.elements import SeasonName

from content import next_uposatha_content, Context, get_context


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


def test_should_provide_today_is_uposatha():
    cal = Calendar()
    today = date(2023, 6, 17)
    uposatha = cal.next_uposatha(today)
    season = cal.current_season(today)
    context = Context(today, SeasonName.RAINY, uposatha, None)
    assert context.today_is_uposatha()


def test_should_create_context_with_no_holiday():
    cal = Calendar()
    today = date(2023, 8, 15)
    uposatha = cal.next_uposatha(today)

    assert uposatha.falls_on == date(2023, 8, 16)

    context = get_context(today)

    assert context.today == date(2023, 8, 15)
    assert context.uposatha == uposatha
    assert context.season == SeasonName.RAINY
    assert context.holiday is None
