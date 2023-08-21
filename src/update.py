from datetime import date

from content import get_context, next_uposatha_content, Context
from compose import next_uposatha
from views import View


def update(today: date):
    context = get_context(today)
    content = next_uposatha_content(context.today)
    next_uposatha(content)


def select_view(context: Context) -> View:
    if context.holiday:
        return View.HOLIDAY

    if context.today_is_uposatha():
        return View.UPOSATHA

    return View.BETWEEN
