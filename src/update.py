from datetime import date

from content import next_uposatha_content
from compose import next_uposatha


def update(today: date):
    content = next_uposatha_content(today)
    next_uposatha(content)
