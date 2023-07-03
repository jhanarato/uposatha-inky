from datetime import date, timedelta

import pytest

from countdown import AppearanceForIconCount, Appearance

def days(number_of_days: int) -> tuple[date, date]:
    start = date(2023, 1, 1)
    end = start + timedelta(days=number_of_days - 1)
    return start, end

def test_should_add_appearance_to_range():
    appearances = AppearanceForIconCount(15)
    appearances[1, 3] = Appearance(1, 2, 3)
    assert appearances[1] == Appearance(1, 2, 3)
    assert appearances[2] == Appearance(1, 2, 3)
    assert appearances[3] == Appearance(1, 2, 3)

def test_should_work_with_any():
    appearances = AppearanceForIconCount(15)
    appearances[1, 3] = Appearance(1, 2, 3)
    assert any(appearances)

def test_should_work_with_all():
    appearances = AppearanceForIconCount(15)
    appearances[1, 14] = Appearance(1, 2, 3)
    assert not all(appearances)
    appearances[15] = Appearance(1, 2, 3)
    assert all(appearances)

def test_should_accept_a_single_icon_count():
    appearances = AppearanceForIconCount(15)
    appearances[1] = Appearance(1, 2, 3)
    assert appearances[1] == Appearance(1, 2, 3)

@pytest.mark.parametrize(
    "index", [-1, 0, 15, 16]
)
def test_should_raise_index_error_on_get(index):
    appearances = AppearanceForIconCount(14)

    with pytest.raises(IndexError):
        a = appearances[index]

@pytest.mark.parametrize(
    "index", [-1, 0, 15, 16]
)
def test_should_raise_index_error_on_set(index):
    appearances = AppearanceForIconCount(14)

    with pytest.raises(IndexError):
        appearances[index] = Appearance(1, 2, 3)

def test_should_allow_overlapping_ranges():
    appearances = AppearanceForIconCount(15)
    appearances[1, 3] = Appearance(1, 2, 3)
    appearances[3, 5] = Appearance(4, 5, 6)
    assert appearances[3] == Appearance(4, 5, 6)
