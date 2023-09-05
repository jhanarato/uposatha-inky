from datetime import date

import pytest
from uposatha.elements import MoonPhase

from components import Text, HorizontalLine
from content import NextUposatha
from countdown import Appearance
from countdown import Countdown
from screen import WIDTH, HEIGHT
from viewer import DrawingViewer
from views import BetweenUposathasView


@pytest.fixture
def content():
    return NextUposatha(
        today=date(2000, 1, 1),
        falls_on=date(2000, 1, 2),
        date="Date formatted", details="Details about uposatha",
        moon_phase=MoonPhase.FULL,
        fourteen_day=False
    )


def test_should_show_between_view(content):
    between_view = BetweenUposathasView(content)
    with DrawingViewer(width=WIDTH, height=HEIGHT, show=False) as draw:
        between_view.show(draw)


def test_should_select_appearances(content):
    between_view = BetweenUposathasView(content)
    appearances = between_view._appearances()
    assert appearances[1] == Appearance(
        BetweenUposathasView.LARGEST_ICON, 8, BetweenUposathasView.GAP
    )


def test_should_generate_components(content):
    between_view = BetweenUposathasView(content)
    component_types = [type(component) for component in between_view._components()]
    assert component_types == [Text, HorizontalLine, Text, Countdown, Text]
