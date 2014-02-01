from agui.awidgets import ALabel
from agui.backends.gtk.widgets import Widget

class Label(Widget, ALabel):
    type = 'Label'

    def __init__(self, item = None):
        ALabel.__init__(self, item)

    @ALabel.text.getter
    def text(self):
        self._text = self.item.get_text()
        return self._text

    @text.setter
    def text(self, value):
        self.item.set_text(value)
        self._text = value
