from agui.awidgets import ASpinBox
from agui.backends.gtk.widgets import Widget

class SpinBox(Widget, ASpinBox):
    type = 'SpinButton'

    def __init__(self, item = None):
        ASpinBox.__init__(self, item)

        self.item.connect('value-changed', self.emit_changed)

    @ASpinBox.value.getter
    def value(self):
        self.value = self.item.get_value()
        return self._value

    @value.setter
    def value(self, value):
        self.item.set_value(value)
        self._value = value
