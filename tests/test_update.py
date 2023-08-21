from datetime import date

from content import get_context
from update import select_view
from views import View


def test_select_between_uposathas_view():
    between_uposathas = date(2023, 8, 2)
    context = get_context(between_uposathas)
    assert select_view(context) == View.BETWEEN


def test_select_uposatha_view():
    uposatha = date(2023, 8, 16)
    context = get_context(uposatha)
    assert select_view(context) == View.UPOSATHA


def test_select_holiday_view():
    asalha_puja = date(2023, 8, 1)
    context = get_context(asalha_puja)
    assert select_view(context) == View.HOLIDAY
