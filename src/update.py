from datetime import date

import views

from content import get_context


def update(today: date):
    context = get_context(today)

    if context.holiday:
        views.holiday(context)

    elif context.today_is_uposatha():
        views.uposatha(context)
    else:
        views.between_uposathas(context)
