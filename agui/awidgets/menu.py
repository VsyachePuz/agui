from agui import Signal
from agui.awidgets import AWidget

class AMenu(AWidget):
    def __init__(self):
        self.triggered = Signal()

        AWidget.__init__(self, self._create_item)

    def emit_triggered(self, *args):
        self.triggered.emit(self.get_text(*args))

    def _create_item(self):
        raise NotImplementedError()

    def append(self, text, icon = None):
        raise NotImplementedError()

    def get_text(self, widget):
        raise NotImplementedError()

    def popup(self, *args):
        raise NotImplementedError()
