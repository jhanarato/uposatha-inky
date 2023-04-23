from typing import List, Tuple
from dataclasses import dataclass
from string import Template
from datetime import date, timedelta
from uposatha.calendar import Calendar

@dataclass
class NextUposatha:
    date: str
    details: str
    countdown: List[str]

def next_uposatha_content(today: date) -> NextUposatha:
    calendar = Calendar()
    uposatha = calendar.next_uposatha(today)
    season = calendar.current_season(today)

    days_since_previous = uposatha.days_since_previous
    uposatha_number = uposatha.number_in_season
    number_of_uposathas = len(season.uposathas)
    season_name = season.name.name.capitalize()

    details = f"{uposatha_number} of {number_of_uposathas} | {season_name} | {days_since_previous} Day"

    return NextUposatha(
        date=uposatha.falls_on.strftime("%a %d/%m/%y"),
        details=details,
        countdown=countdown_letters(today, uposatha.falls_on)
    )

def countdown_letters(today: date, uposatha_date: date) -> List[str]:
    day_letters = []
    next_date = today
    while next_date <= uposatha_date:
        day_letter = next_date.strftime("%a")[0]
        day_letters.append(day_letter)
        next_date += timedelta(1)
    return day_letters
