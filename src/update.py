from datetime import date

from content import get_context, next_uposatha_content
from compose import next_uposatha


def update(today: date):
    context = get_context(today)
    content = next_uposatha_content(context.today)
    next_uposatha(content)
