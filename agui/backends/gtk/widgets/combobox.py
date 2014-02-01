from agui.awidgets import AComboBox
from agui.backends.gtk.widgets import Widget

class ComboBox(Widget, AComboBox):
    type = 'ComboBoxText'

    def __init__(self, item = None):
        AComboBox.__init__(self, item)

        self.item.connect('changed', self.emit_changed)

    def clear(self):
        self.item.get_model().clear()
        AComboBox.clear(self)

    def append(self, text):
        self.item.append_text(text)
        AComboBox.append(self, text)

    def prepend(self, text):
        self.item.prepend_text(text)
        AComboBox.prepend(self, text)

    def remove(self, index):
        self.item.remove(index)
        AComboBox.remove(self, index)

    def insert(self, index, text):
        self.item.insert_text(index, text)
        AComboBox.insert(self, index, text)

    @AComboBox.selected.getter
    def selected(self):
        self._selected = self.item.get_active()
        return self._selected

    @selected.setter
    def selected(self, value):
        self.item.set_active(value)
        self._selected = value

    @AComboBox.selected_text.getter
    def selected_text(self):
        return self.item.get_active_text()
