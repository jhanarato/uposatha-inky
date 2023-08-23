from datetime import date

import views
from content import get_context


def update(today: date):
    context = get_context(today)

    if context.holiday_today():
        views.holiday(context)
    elif context.uposatha_today():
        views.uposatha(context)
    else:
        views.between_uposathas(context)
