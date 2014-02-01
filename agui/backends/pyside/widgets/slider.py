from agui.awidgets import ASlider
from agui.backends.pyside.widgets import Widget

class Slider(Widget, ASlider):
    type = 'QSlider'

    def __init__(self, item = None):
        ASlider.__init__(self, item)

        self.item.valueChanged.connect(self.emit_changed)

    @ASlider.value.getter
    def value(self):
        self._value = self.item.value()
        return self._value

    @value.setter
    def value(self, value):
        self.item.setValue(value)
        self._value = value
