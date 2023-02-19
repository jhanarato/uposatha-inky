from datetime import date

from content import (
    next_uposatha_content, NextUposathaContent
)

def test_next_uposatha_content_line_one():
    today = date(2023, 2, 13)
    lines = next_uposatha_content(today)
    assert lines[0] == "Sun 19/02 (6 days)"
