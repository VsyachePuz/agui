from agui import Signal
from agui.awidgets import AWidget

class AComboBox(AWidget):
    def __init__(self, item = None):
        self._list = []
        self._selected = 0
        self.changed = Signal()

        AWidget.__init__(self, item)

    def emit_changed(self, *args):
        self.changed.emit(self.selected)

    def clear(self):
        self._list = []

    def append(self, text):
        self._list.append(text)

    def prepend(self, text):
        self._list.insert(0, text)

    def remove(self, index):
        self._list.remove(index)

    def insert(self, index, text):
        self._list.insert(index, text)

    @property
    def items(self):
        return self._list

    @items.setter
    def items(self, items):
        self.clear()
        for item in items:
            self.append(item)

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, value):
        self._selected = value

    @property
    def selected_text(self):
        return self._list[self.selected]

    @selected_text.setter
    def selected_text(self, value):
        index = 0
        for item in self._list:
            if text == item:
                self.selected = index
                break

            index += 1
