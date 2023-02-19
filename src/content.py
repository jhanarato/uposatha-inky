from typing import List

from dataclasses import dataclass
from datetime import date
from uposatha.calendar import Calendar
from uposatha.elements import Season, Uposatha

def next_uposatha_content(today: date) -> List[str]:
    calendar = Calendar()
    uposatha = calendar.next_uposatha(today)
    season = calendar.current_season(today)

    return [
        date_line(uposatha, today),
        season_line(season, uposatha)
    ]

def date_line(next_uposatha, today):
    days_until = (next_uposatha.falls_on - today).days
    falls_on = next_uposatha.falls_on.strftime("%a %d/%m")
    line_one = f"{falls_on} ({days_until} days)"
    return line_one

def season_line(season: Season, uposatha: Uposatha):
    text = f"{uposatha.days_since_previous} day, "
    text += f"{uposatha.number_in_season}/{len(season.uposathas)} "
    text += f"{season.name.name.capitalize()} Season"
    return text
