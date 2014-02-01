from agui import Signal
from agui.awidgets import AWidget

class ASpinBox(AWidget):
    def __init__(self, item = None):
        self._value = 0
        self.changed = Signal()

        AWidget.__init__(self, item)

    def emit_changed(self, *args):
        self.changed.emit(self.value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
