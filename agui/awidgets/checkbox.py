from agui import Signal
from agui.awidgets import AWidget

class ACheckBox(AWidget):
    def __init__(self, item = None):
        self._checked = False
        self.changed = Signal()

        AWidget.__init__(self, item)

    def emit_changed(self, *args):
        self.changed.emit(self.checked)

    @property
    def checked(self):
        return self._checked

    @checked.setter
    def checked(self, value):
        self._checked = value
