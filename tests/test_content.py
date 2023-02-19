from datetime import date

from content import next_uposatha_content

def test_line_one():
    today = date(2023, 2, 13)
    lines = next_uposatha_content(today)
    assert lines[0] == "Sun 19/02 (15 Day)"

def test_line_two():
    today = date(2023, 2, 13)
    lines = next_uposatha_content(today)
    assert lines[1] == "7/8 Cold Season"