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
        line_one(uposatha, today),
        line_two(season, uposatha)
    ]

def line_one(uposatha, today):
    formatted_date = uposatha.falls_on.strftime("%a %d/%m")
    text = f"{formatted_date} ({uposatha.days_since_previous} Day)"
    return text

def line_two(season: Season, uposatha: Uposatha):
    text = (
        f"{uposatha.number_in_season}/{len(season.uposathas)} "
        f"{season.name.name.capitalize()} Season"
    )
    return text
