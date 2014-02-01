from agui.awidgets import ALabel
from agui.backends.pyside.widgets import Widget

class Label(Widget, ALabel):
    type = 'QLabel'

    def __init__(self, item = None):
        ALabel.__init__(self, item)

    @ALabel.text.getter
    def text(self):
        self._text = self.item.text()
        return self._text

    @text.setter
    def text(self, value):
        self.item.setText(value)
        self._text = value
