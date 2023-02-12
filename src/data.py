from dataclasses import dataclass
from datetime import date
from uposatha.calendar import Calendar
from pprint import pprint

@dataclass(frozen=True)
class NextUposathaView:
    today: date
    season: str
    falls_on: date
    moon_phase: str
    of_the_day: str
    uposatha_number: int
    number_of_uposathas: int

    @property
    def today_is_the_uposatha(self) -> bool:
        return self.today == self.falls_on

    @property
    def days_until(self) -> int:
        return (self.falls_on - self.today).days

def next_uposatha_view(calendar: Calendar, today: date) -> NextUposathaView:
    season = calendar.current_season(today)
    uposatha = calendar.next_uposatha(today)

    if uposatha.days_since_previous == 15:
        uposatha_day = "fifteen"
    else:
        uposatha_day = "fourteen"

    return NextUposathaView(
        today=date.today(),
        season=season.name.name,
        falls_on=uposatha.falls_on,
        moon_phase=uposatha.moon_phase.name,
        of_the_day=uposatha_day,
        uposatha_number=uposatha.number_in_season,
        number_of_uposathas=len(season.uposathas)
    )
