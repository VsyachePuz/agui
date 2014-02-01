from agui import Signal
from agui.awidgets import AWidget

class AIndicator(AWidget):
    def __init__(self, window, name, menu, attention_icon, passive_icon):
        self._window = window
        self._name = name
        self._menu = menu
        self._attention = False
        self._hidden = False
        self._attention_icon = attention_icon
        self._passive_icon = passive_icon

        self.triggered = Signal()

        AWidget.__init__(self, self._create_item)

    def _create_item(self):
        raise NotImplementedError()

    def emit_triggered(self, *arg):
        self.triggered.emit()

    @property
    def attention(self):
        return self._attention

    @attention.setter
    def attention(self, value):
        self._attention = value

    @property
    def hidden(self):
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        self._hidden = value

    def hide(self):
        self.hidden = True

    def show(self):
        self.hidden = False

    @property
    def attention_icon(self):
        return self._attention_icon

    @attention_icon.setter
    def attention_icon(self, value):
        self._attention_icon = value

    @property
    def passive_icon(self):
        return self._passive_icon

    @passive_icon.setter
    def passive_icon(self, value):
        self._passive_icon = value
