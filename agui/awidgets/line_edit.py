from agui import Signal
from agui.awidgets import AWidget

class ALineEdit(AWidget):
    def __init__(self, item = None):
        self._has_clear = False
        self._has_error = False
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

    def clear(self):
        self.text = ''

    @property
    def has_clear(self):
        return self._has_clear

    @has_clear.setter
    def has_clear(self, value):
        self._has_clear = value

    @property
    def has_error(self):
        return self._has_error

    @has_error.setter
    def has_error(self, value):
        self._has_error = value

    def focus(self):
        raise NotImplementedError()

    def hide_error(self):
        raise NotImplementedError()

    def show_error(self, name = None):
        raise NotImplementedError()
