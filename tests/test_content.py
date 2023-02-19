from datetime import date

from content import next_uposatha_content

def test_date_line():
    today = date(2023, 2, 13)
    lines = next_uposatha_content(today)
    assert lines[0] == "Sun 19/02 (6 days)"

def test_season_line():
    today = date(2023, 2, 13)
    lines = next_uposatha_content(today)
    assert lines[1] == "14 day, 7/8 Cold Season"