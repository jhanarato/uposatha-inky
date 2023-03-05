from typing import List

from images import DrawingConfig, Text

class Layout:
    def __init__(self, drawing: DrawingConfig):
        self._drawing: DrawingConfig = drawing
        self.items: List[Text] = []

    def add_text(self, text: Text):
        self.center(text)
        self.items.append(text)

    def center(self, text: Text):
        text.x = round((self._drawing.width - text.width) / 2)

    def draw(self):
        pass
