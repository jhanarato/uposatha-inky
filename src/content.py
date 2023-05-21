from typing import List
from dataclasses import dataclass
from datetime import date

import uposatha.elements
from uposatha.calendar import Calendar
from uposatha.elements import MoonPhase

from countdown import countdown_letters


@dataclass
class NextUposatha:
    falls_on: date
    date: str
    details: str
    countdown: List[str]
    moon_phase: uposatha.elements.MoonPhase

def next_uposatha_content(today: date) -> NextUposatha:
    calendar = Calendar()
    next_uposatha = calendar.next_uposatha(today)
    season = calendar.current_season(today)

    return NextUposatha(
        falls_on=next_uposatha.falls_on,
        date=next_uposatha.falls_on.strftime("%a %d/%m/%y"),
        details=uposatha_details(season, next_uposatha),
        countdown=countdown_letters(today, next_uposatha.falls_on),
        moon_phase=MoonPhase.FULL
    )

def uposatha_details(season, next_uposatha):
    days_since_previous = next_uposatha.days_since_previous
    uposatha_number = next_uposatha.number_in_season
    number_of_uposathas = len(season.uposathas)
    season_name = season.name.name.capitalize()
    return f"{uposatha_number} of {number_of_uposathas} | {season_name} | {days_since_previous} Day"

