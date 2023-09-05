from datetime import date

import pytest
from uposatha.elements import MoonPhase

from content import NextUposatha
from countdown import Appearance
from screen import WIDTH, HEIGHT
from viewer import DrawingViewer
from views import BetweenUposathasView


@pytest.fixture
def fifteen_day_content():
    return NextUposatha(
        today=date(2000, 1, 1),
        falls_on=date(2000, 1, 2),
        date="Date formatted", details="Details about uposatha",
        moon_phase=MoonPhase.FULL,
        fourteen_day=False
    )


def test_should_show_between_view(fifteen_day_content):
    between_view = BetweenUposathasView(fifteen_day_content)
    with DrawingViewer(width=WIDTH, height=HEIGHT, show=False) as draw:
        between_view.show(draw)


def test_should_select_fifteen_day_appearances(fifteen_day_content):
    between_view = BetweenUposathasView(fifteen_day_content)
    appearances = between_view._appearances()
    assert appearances[1] == Appearance(
        BetweenUposathasView.LARGEST_ICON, 8, BetweenUposathasView.GAP
    )
