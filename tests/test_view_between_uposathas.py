from datetime import date

import pytest

from components import Text, HorizontalLine
from content import get_context
from countdown import Appearance
from countdown import Countdown
from screen import WIDTH, HEIGHT
from viewer import DrawingViewer
from views import select_view, BetweenUposathasView, next_uposatha_content


@pytest.fixture
def day_before_uposatha_context():
    return get_context(date(2023, 9, 30))


def test_should_show_between_view(day_before_uposatha_context):
    content = next_uposatha_content(day_before_uposatha_context)
    between_view = BetweenUposathasView()
    with DrawingViewer(width=WIDTH, height=HEIGHT, show=False) as draw:
        between_view.show(draw, day_before_uposatha_context)


def test_should_select_appearances(day_before_uposatha_context):
    content = next_uposatha_content(day_before_uposatha_context)
    between_view = BetweenUposathasView()
    appearances = between_view._appearances(content)
    assert appearances[1] == Appearance(
        BetweenUposathasView.LARGEST_ICON, 8, BetweenUposathasView.GAP
    )


def test_should_generate_components(day_before_uposatha_context):
    content = next_uposatha_content(day_before_uposatha_context)
    between_view = BetweenUposathasView()
    component_types = [type(component) for component in between_view._components(content)]
    assert component_types == [Text, HorizontalLine, Text, Countdown, Text]


def test_should_layout_components(day_before_uposatha_context):
    content = next_uposatha_content(day_before_uposatha_context)
    between_view = BetweenUposathasView()
    layout = between_view._layout(content)
    assert sum(1 for _ in layout.coordinates()) == len(between_view._components(content))


def test_should_select_between_view(day_before_uposatha_context):
    assert isinstance(select_view(day_before_uposatha_context), BetweenUposathasView)
