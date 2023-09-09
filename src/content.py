from dataclasses import dataclass
from datetime import date
from typing import Optional

from uposatha.calendar import Calendar
from uposatha.elements import MoonPhase, Season, Uposatha, Holiday


@dataclass(frozen=True)
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


class BetweenUposathasContent:
    def __init__(self, context: Context):
        self._context = context

    @property
    def today(self) -> date:
        return self._context.today

    @property
    def falls_on(self) -> date:
        return self._context.uposatha.falls_on

    @property
    def date(self) -> str:
        return self._context.uposatha.falls_on.strftime("%A %d/%m/%y")

    @property
    def moon_phase(self) -> MoonPhase:
        return self._context.uposatha.moon_phase

    @property
    def fourteen_day(self) -> bool:
        return self._context.uposatha.days_since_previous == 14

    @property
    def details(self) -> str:
        days_since_previous = self._context.uposatha.days_since_previous
        uposatha_number = self._context.uposatha.number_in_season
        number_of_uposathas = len(self._context.season.uposathas)
        season_name = self._context.season.name.name.capitalize()
        return f"{uposatha_number} of {number_of_uposathas} | {season_name} | {days_since_previous} Day"
