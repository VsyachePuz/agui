from agui import APP, Signal
from agui.awidgets import AWidget

class AButton(AWidget):
    def __init__(self, item = None):
        self._text = ''
        self._icon = None
        self.pressed = Signal()

        AWidget.__init__(self, item)

    def emit_pressed(self, *args):
        self.pressed.emit()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
