from datetime import date, timedelta

import pytest

from countdown import IconCountMapping, Appearance

def days(number_of_days: int) -> tuple[date, date]:
    start = date(2023, 1, 1)
    end = start + timedelta(days=number_of_days - 1)
    return start, end

def test_should_add_appearance_to_range():
    appearances = IconCountMapping[Appearance](15)
    appearances[1, 3] = Appearance(1, 2, 3)
    assert appearances[1] == Appearance(1, 2, 3)
    assert appearances[2] == Appearance(1, 2, 3)
    assert appearances[3] == Appearance(1, 2, 3)

def test_should_be_any():
    appearances = IconCountMapping[Appearance](15)
    appearances[3] = Appearance(1, 2, 3)
    assert any(appearances)

def test_should_not_be_any():
    appearances = IconCountMapping[Appearance](15)
    assert not any(appearances)

def test_should_be_all_when_all_assigned():
    appearances = IconCountMapping[Appearance](15)
    appearances[1, 15] = Appearance(1, 2, 3)
    appearances[15] = Appearance(1, 2, 3)
    assert all(appearances)

def should_not_be_all_when_one_missing():
    appearances = IconCountMapping[Appearance](15)
    appearances[1, 14] = Appearance(1, 2, 3)
    assert not all(appearances)


def test_should_accept_a_single_icon_count():
    appearances = IconCountMapping[Appearance](15)
    appearances[1] = Appearance(1, 2, 3)
    assert appearances[1] == Appearance(1, 2, 3)

@pytest.mark.parametrize(
    "index", [-1, 0, 15, 16]
)
def test_should_raise_index_error_on_get(index):
    appearances = IconCountMapping[Appearance](14)

    with pytest.raises(KeyError):
        a = appearances[index]

@pytest.mark.parametrize(
    "index", [-1, 0, 15, 16]
)
def test_should_raise_index_error_on_set(index):
    appearances = IconCountMapping[Appearance](14)

    with pytest.raises(KeyError):
        appearances[index] = Appearance(1, 2, 3)

def test_should_allow_overlapping_ranges():
    appearances = IconCountMapping[Appearance](15)
    appearances[1, 3] = Appearance(1, 2, 3)
    appearances[3, 5] = Appearance(4, 5, 6)
    assert appearances[3] == Appearance(4, 5, 6)

def test_should_delete_existing():
    appearances = IconCountMapping[Appearance](15)
    appearances[1, 15] = Appearance(1, 2, 3)
    assert appearances[2] == Appearance(1, 2, 3)
    del(appearances[2])
    with pytest.raises(KeyError):
        _ = appearances[2]

def test_should_raise_on_deleting_missing():
    appearances = IconCountMapping[Appearance](15)
    appearances[1, 15] = Appearance(1, 2, 3)
    del appearances[6]
    with pytest.raises(KeyError):
        del appearances[6]
