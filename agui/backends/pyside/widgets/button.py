from agui import APP
from agui.awidgets import AButton
from agui.backends.pyside.widgets import Widget

class Button(Widget, AButton):
    type = 'QPushButton'

    def __init__(self, item = None):
        AButton.__init__(self, item)

        self.item.pressed.connect(self.emit_pressed)

    @AButton.text.getter
    def text(self):
        self._text = self.item.text()
        return self._text

    @text.setter
    def text(self, value):
        self.item.setText(value)
        self._text = value

    @AButton.icon.setter
    def icon(self, value):
        self.item.setIcon(value.icon())
        self._icon = value
