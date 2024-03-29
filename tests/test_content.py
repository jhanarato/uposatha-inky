from datetime import date

import pytest
from uposatha.calendar import Calendar
from uposatha.elements import SeasonName, HolidayName

from content import Content, Context, get_context


@pytest.mark.parametrize(
    "today,is_fourteen_day",
    [
        (date(2011, 1, 3), True),
        (date(2011, 1, 4), True),
        (date(2011, 1, 5), False),
    ]
)
def test_should_flag_fourteen_day(today, is_fourteen_day):
    context = get_context(today)
    assert Content(context).fourteen_day == is_fourteen_day


def test_should_format_details():
    context = get_context(date(2023, 9, 10))
    content = Content(context)
    assert content.details == "3 of 8 | Rainy | 14 Day"


def test_should_provide_today_is_uposatha():
    cal = Calendar()
    today = date(2023, 6, 17)
    uposatha = cal.next_uposatha(today)
    season = cal.current_season(today)
    context = Context(today, season, uposatha, None)
    assert context.uposatha_today()


def test_should_create_context_with_no_holiday():
    cal = Calendar()
    today = date(2023, 8, 15)
    uposatha = cal.next_uposatha(today)

    assert uposatha.falls_on == date(2023, 8, 16)

    context = get_context(today)

    assert context.today == date(2023, 8, 15)
    assert context.uposatha == uposatha
    assert context.season.name == SeasonName.RAINY
    assert context.holiday is None


def test_context_for_day_before_holiday():
    day_before_asalha = date(2023, 7, 31)
    context = get_context(day_before_asalha)
    assert context.today == day_before_asalha
    assert context.uposatha.falls_on == date(2023, 8, 1)
    assert context.holiday.name == HolidayName.ASALHA


def test_context_for_day_before_ordinary_uposatha():
    day_before_new_moon_after_asalha = date(2023, 8, 15)
    context = get_context(day_before_new_moon_after_asalha)
    assert context.today == day_before_new_moon_after_asalha
    assert context.uposatha.falls_on == date(2023, 8, 16)
    assert context.holiday is None


@pytest.mark.parametrize(
    "today,is_uposatha",
    [
        (date(2023, 7, 31), False),
        (date(2023, 8, 1), True),
        (date(2023, 8, 15), False),
        (date(2023, 8, 16), True),
    ]
)
def test_context_uposatha_today(today, is_uposatha):
    assert get_context(today).uposatha_today() == is_uposatha


@pytest.mark.parametrize(
    "today,is_holiday",
    [
        (date(2023, 7, 31), False),
        (date(2023, 8, 1), True),
        (date(2023, 8, 15), False),
        (date(2023, 8, 16), False),
    ]
)
def test_context_uposatha_today(today, is_holiday):
    assert get_context(today).holiday_today() == is_holiday


@pytest.mark.parametrize(
    "today,words",
    [
        (date(2023, 9, 18), ("", "")),
        (date(2023, 9, 14), ("New", "Moon")),
        (date(2023, 9, 29), ("Full", "Moon")),
        (date(2023, 3, 6), ("Māgha", "Pūjā")),
        (date(2023, 6, 3), ("Visākha", "Pūjā")),
        (date(2023, 8, 1), ("Āsāḷha", "Pūjā")),
        (date(2023, 10, 29), ("Pavāraṇā", "Day")),
    ]
)
def test_moon_words(today, words):
    context = get_context(today)
    content = Content(context)
    assert content.moon_words == words


@pytest.mark.parametrize(
    "today,is_uposatha",
    [
        (date(2023, 9, 18), False),
        (date(2023, 9, 29), True),
    ]
)
def test_is_uposatha(today, is_uposatha):
    context = get_context(today)
    content = Content(context)
    assert content.is_uposatha == is_uposatha
