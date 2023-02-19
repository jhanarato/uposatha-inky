from typing import List

from dataclasses import dataclass
from datetime import date
from uposatha.calendar import Calendar

@dataclass(frozen=True)
class NextUposathaContent:
    day: str
    date: str
    days_until: str

def next_uposatha_content(today: date) -> List[str]:
    calendar = Calendar()
    next_uposatha = calendar.next_uposatha(today)

    days_until = (next_uposatha.falls_on - today).days
    falls_on = next_uposatha.falls_on.strftime("%a %d/%m")

    line_one = f"{falls_on} ({days_until} days)"
    return [line_one]
