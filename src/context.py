from dataclasses import dataclass
from datetime import date
from typing import Optional

from uposatha.calendar import Calendar
from uposatha.elements import Uposatha, Holiday, Season


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
