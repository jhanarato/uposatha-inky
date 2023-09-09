from datetime import date

import screen
from content import get_context
from viewer import DrawingViewer
from views import select_view


def update(today: date):
    context = get_context(today)
    view = select_view(context)
    with DrawingViewer(width=screen.WIDTH, height=screen.HEIGHT) as draw:
        view.show(draw)
