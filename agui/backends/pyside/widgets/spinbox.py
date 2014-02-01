from agui.awidgets import ASpinBox
from agui.backends.pyside.widgets import Widget

class SpinBox(Widget, ASpinBox):
    type = 'QSpinBox'

    def __init__(self, item = None):
        ASpinBox.__init__(self, item)

        self.item.valueChanged.connect(self.emit_changed)

    @ASpinBox.value.getter
    def value(self):
        self.value = self.item.value()
        return self._value

    @value.setter
    def value(self, value):
        self.item.setValue(value)
        self._value = value
