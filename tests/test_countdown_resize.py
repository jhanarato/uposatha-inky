from datetime import date, timedelta

import pytest

from countdown import (
    zoom_on_approach, AppearanceForIconCount,
    GAP, LARGE_ICON, Appearance
)

def days(number_of_days: int) -> tuple[date, date]:
    start = date(2023, 1, 1)
    end = start + timedelta(days=number_of_days - 1)
    return start, end

@pytest.mark.parametrize(
    "fourteen_day,length",
    [
        (True, 14),
        (False, 15),
    ]
)
def test_should_be_of_correct_length(fourteen_day, length):
    appearances = AppearanceForIconCount(fourteen_day=fourteen_day)
    assert len(appearances) == length

def test_should_add_appearance_to_range():
    appearances = AppearanceForIconCount(fourteen_day=False)
    appearances[1, 3] = Appearance(1, 2, 3)
    assert appearances[1] == Appearance(1, 2, 3)
    assert appearances[2] == Appearance(1, 2, 3)
    assert appearances[3] == Appearance(1, 2, 3)

def test_should_work_with_any():
    appearances = AppearanceForIconCount(fourteen_day=False)
    appearances[1, 3] = Appearance(1, 2, 3)
    assert any(appearances)

def test_should_work_with_all():
    appearances = AppearanceForIconCount(fourteen_day=False)
    appearances[1, 14] = Appearance(1, 2, 3)
    assert not all(appearances)
    appearances[15, 15] = Appearance(1, 2, 3)
    assert all(appearances)
