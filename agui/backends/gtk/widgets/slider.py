from agui.awidgets import ASlider
from agui.backends.gtk.widgets import Widget

class Slider(Widget, ASlider):
    type = 'Scale'

    def __init__(self, item = None):
        ASlider.__init__(self, item)

        self.item.connect('value-changed', self.emit_changed)

    @ASlider.value.getter
    def value(self):
        self._value = self.item.get_value()
        return self._value

    @value.setter
    def value(self, value):
        self.item.set_value(value)
        self._value = value
