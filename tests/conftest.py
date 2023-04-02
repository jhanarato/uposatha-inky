import pytest

from components import Countdown
from test_countdown import LetterSpy


def letters_to_letter_spy(letters: list[str], size: int) -> list[LetterSpy]:
    return [LetterSpy(size=size) for letter in letters]


@pytest.fixture
def one_day_countdown():
    component = Countdown([])
    component._icons = letters_to_letter_spy(letters=["M"], size=10)
    return component


@pytest.fixture
def three_day_countdown():
    component = Countdown([])
    component._icons = letters_to_letter_spy(letters=["M", "T", "W"], size=10)
    return component
