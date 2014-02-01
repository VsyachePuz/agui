from agui import APP
from agui.awidgets import AButton
from agui.backends.gtk.widgets import Widget

class Button(Widget, AButton):
    type = 'Button'

    def __init__(self, item = None):
        AButton.__init__(self, item)

        self.item.connect('button-press-event', self.emit_pressed)

    @AButton.text.getter
    def text(self):
        self._text = self.item.get_label()
        return self._text

    @text.setter
    def text(self, value):
        self.item.set_label(value)
        self._text = value

    @AButton.icon.setter
    def icon(self, value):
        self.item.set_image(value.icon())
        self._icon = value
