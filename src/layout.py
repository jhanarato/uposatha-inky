from typing import List

from images import Text

class Layout:
    def __init__(self):
        self.items: List[Text] = []

    def add_text(self, text: Text):
        self.items.append(text)

    def draw(self):
        pass