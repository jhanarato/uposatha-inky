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


class Content:
    def __init__(self, context: Context):
        self._context = context

    @property
    def today(self) -> date:
        return self._context.today

    @property
    def falls_on(self) -> date:
        return self._context.uposatha.falls_on

    @property
    def is_uposatha(self) -> bool:
        return self._context.uposatha_today()

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
    def days_since_uposatha(self) -> int:
        return self._context.uposatha.days_since_previous

    @property
    def uposatha_number(self) -> int:
        return self._context.uposatha.number_in_season

    @property
    def number_of_uposathas(self) -> int:
        return len(self._context.season.uposathas)

    @property
    def num_of_num(self) -> str:
        return f"{self.uposatha_number} of {self.number_of_uposathas}"

    @property
    def season_name(self) -> str:
        return self._context.season.name.name.capitalize()

    @property
    def day(self) -> str:
        return f"{self.days_since_uposatha} Day"

    @property
    def details(self) -> str:
        return f"{self.num_of_num} | {self.season_name} | {self.day}"

    @property
    def moon_words(self) -> tuple[str, str]:
        if not self.is_uposatha:
            return "", ""

        return "Full", "Moon"
