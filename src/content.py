from string import Template
from datetime import date
from uposatha.calendar import Calendar

def next_uposatha_content(today: date) -> str:
    calendar = Calendar()
    uposatha = calendar.next_uposatha(today)
    season = calendar.current_season(today)

    template = Template(
        "${formatted_date} (${days_since_previous} Day)\n"
        "${uposatha_number}/${number_of_uposathas} "
        "${season_name} Season"
    )

    return template.substitute(
        formatted_date=uposatha.falls_on.strftime("%a %d/%m"),
        days_since_previous=uposatha.days_since_previous,
        uposatha_number=uposatha.number_in_season,
        number_of_uposathas=len(season.uposathas),
        season_name=season.name.name.capitalize()
    )
