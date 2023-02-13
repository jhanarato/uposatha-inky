from dataclasses import dataclass
from datetime import date
from uposatha.calendar import Calendar

@dataclass(frozen=True)
class NextUposathaContent:
    day: str
    date: str
    days_until: str

def next_uposatha_content(today: date) -> NextUposathaContent:
    calendar = Calendar()
    next_uposatha = calendar.next_uposatha(today)

    days_until = (next_uposatha.falls_on - today).days

    return NextUposathaContent(
        day = next_uposatha.falls_on.strftime("%A"),
        date = next_uposatha.falls_on.strftime("%d/%m/%y"),
        days_until = f"In {days_until} days"
    )
