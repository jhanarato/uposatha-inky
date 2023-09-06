from dataclasses import dataclass
from datetime import date
from typing import Optional

from uposatha.calendar import Calendar
from uposatha.elements import Uposatha, MoonPhase, Holiday, Season


@dataclass
class Context:
    today: date
    season: Season
    uposatha: Uposatha
    holiday: Optional[Holiday]

    def uposatha_today(self) -> bool:
        return self.today == self.uposatha.falls_on

    def holiday_today(self) -> bool:
        if self.holiday is None:
            return False

        return self.uposatha_today()


def get_context(today: date) -> Context:
    cal = Calendar()
    uposatha = cal.next_uposatha(today)
    season = cal.current_season(today)
    return Context(today, season, uposatha, uposatha.holiday)


@dataclass
class NextUposatha:
    today: date
    falls_on: date
    date: str
    details: str
    moon_phase: MoonPhase
    fourteen_day: bool


def next_uposatha_content(today: date) -> NextUposatha:
    calendar = Calendar()
    next_uposatha = calendar.next_uposatha(today)
    season = calendar.current_season(today)

    return NextUposatha(
        today=today,
        falls_on=next_uposatha.falls_on,
        date=next_uposatha.falls_on.strftime("%A %d/%m/%y"),
        details=uposatha_details(season, next_uposatha),
        moon_phase=next_uposatha.moon_phase,
        fourteen_day=(next_uposatha.days_since_previous == 14)
    )


def uposatha_details(season, next_uposatha):
    days_since_previous = next_uposatha.days_since_previous
    uposatha_number = next_uposatha.number_in_season
    number_of_uposathas = len(season.uposathas)
    season_name = season.name.name.capitalize()
    return f"{uposatha_number} of {number_of_uposathas} | {season_name} | {days_since_previous} Day"
