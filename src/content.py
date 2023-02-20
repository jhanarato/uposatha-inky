from typing import List

from string import Template
from datetime import date, timedelta
from uposatha.calendar import Calendar

def next_uposatha_content(today: date) -> str:
    calendar = Calendar()
    uposatha = calendar.next_uposatha(today)
    season = calendar.current_season(today)

    template = Template(
        "${formatted_date}"
        "\n${uposatha_number}/${number_of_uposathas} "
        "${season_name} Season"
        "\n${days_since_previous} Day ${phase} Moon"
    )

    return template.substitute(
        formatted_date=uposatha.falls_on.strftime("%A, %d %B"),
        days_since_previous=uposatha.days_since_previous,
        uposatha_number=uposatha.number_in_season,
        number_of_uposathas=len(season.uposathas),
        season_name=season.name.name.capitalize(),
        phase=uposatha.moon_phase.name.capitalize()
    )

def countdown(today: date, uposatha_date: date) -> List[str]:
    day_letters = []
    next_date = today
    while next_date <= uposatha_date:
        day_letter = next_date.strftime("%a")[0]
        day_letters.append(day_letter)
        next_date += timedelta(1)
    return day_letters
