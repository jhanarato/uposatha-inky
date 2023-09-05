from screen import WIDTH, HEIGHT
from viewer import DrawingViewer
from views import BetweenUposathasView


def test_should_show_between_view():
    between_view = BetweenUposathasView()
    with DrawingViewer(width=WIDTH, height=HEIGHT, show=False) as draw:
        between_view.show(draw)
