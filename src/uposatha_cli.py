from datetime import date
from uposatha.calendar import Calendar

calendar = Calendar()

season = calendar.current_season()
uposatha = calendar.next_uposatha()

season_name = season.name.name.lower()

today = date.today().isoformat()
falls_on = uposatha.falls_on.isoformat()

phase = uposatha.moon_phase.name

if uposatha.days_since_previous == 15:
    uposatha_day = "fifteen day"
else:
    uposatha_day = "fourteen day"

number = f"{uposatha.number_in_season}/{len(season.uposathas)}"

print(f"{today}")
print(f"Next Uposatha: {falls_on} {uposatha_day} {number} of the {season_name} season.")