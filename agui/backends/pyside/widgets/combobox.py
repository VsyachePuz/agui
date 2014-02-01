from agui.awidgets import AComboBox
from agui.backends.pyside.widgets import Widget

class ComboBox(Widget, AComboBox):
    type = 'QComboBox'

    def __init__(self, item = None):
        AComboBox.__init__(self, item)

        self.item.currentIndexChanged.connect(self.emit_changed)

    def clear(self):
        self.item.clear()
        AComboBox.clear(self)

    def append(self, text):
        self.item.addItem(text)
        AComboBox.append(self, text)

    def prepend(self, text):
        self.item.insertItem(0, text)
        AComboBox.prepend(self, text)

    def remove(self, index):
        self.item.removeItem(index)
        AComboBox.remove(self, index)

    def insert(self, index, text):
        self.item.insertItem(index, text)
        AComboBox.insert(self, index, text)

    @AComboBox.selected.getter
    def selected(self):
        self._selected = self.item.currentIndex()
        return self._selected

    @selected.setter
    def selected(self, value):
        self.item.setCurrentIndex(value)
        self._selected = value

    @AComboBox.selected_text.getter
    def selected_text(self):
        return self.item.currentText()
