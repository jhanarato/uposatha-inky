from datetime import date

import pytest

from components import Text, HorizontalLine
from content import get_context
from countdown import Appearance
from countdown import Countdown
from screen import WIDTH, HEIGHT
from viewer import DrawingViewer
from views import select_view, BetweenUposathasView, next_uposatha_content, UposathaView, HolidayView


@pytest.fixture
def day_before_uposatha_context():
    return get_context(date(2023, 9, 28))


@pytest.fixture
def uposatha_context():
    return get_context(date(2023, 9, 29))


@pytest.fixture
def holiday_context():
    return get_context(date(2023, 10, 29))


def test_should_show_between_view(day_before_uposatha_context):
    between_view = BetweenUposathasView(day_before_uposatha_context)
    with DrawingViewer(width=WIDTH, height=HEIGHT, show=False) as draw:
        between_view.show(draw, day_before_uposatha_context)


def test_should_select_appearances(day_before_uposatha_context):
    between_view = BetweenUposathasView(day_before_uposatha_context)
    appearances = between_view._appearances()
    assert appearances[1] == Appearance(
        BetweenUposathasView.LARGEST_ICON, 8, BetweenUposathasView.GAP
    )


def test_should_generate_components(day_before_uposatha_context):
    between_view = BetweenUposathasView(day_before_uposatha_context)
    component_types = [type(component) for component in between_view._components()]
    assert component_types == [Text, HorizontalLine, Text, Countdown, Text]


def test_should_layout_components(day_before_uposatha_context):
    content = next_uposatha_content(day_before_uposatha_context)
    between_view = BetweenUposathasView(day_before_uposatha_context)
    layout = between_view._layout(content)
    assert sum(1 for _ in layout.coordinates()) == len(between_view._components())


@pytest.mark.parametrize(
    "today,view_type",
    [
        (date(2023, 9, 28), BetweenUposathasView),
        (date(2023, 9, 29), UposathaView),
        (date(2023, 10, 29), HolidayView),
    ]
)
def test_should_select_view_from_context(today, view_type):
    context = get_context(today)
    view = select_view(context)
    assert isinstance(view, view_type)
