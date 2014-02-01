from agui import Signal
from agui.awidgets import AWidget

class ATextArea(AWidget):
    def __init__(self, item = None):
        self._text = ''
        self.changed = Signal()

        AWidget.__init__(self, item)

    def emit_changed(self, *args):
        self.changed.emit(self.text)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def insert(self, text):
        raise NotImplementedError()

    def clear(self):
        self.text = ''
