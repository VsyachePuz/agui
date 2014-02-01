from agui.backends.pyside.imports import *
from agui.awidgets import AIndicator
from agui.backends.pyside.widgets import Widget

class Indicator(Widget, AIndicator):
    def __init__(self, window, name, menu, attention_icon, passive_icon):
        AIndicator.__init__(self, window, name, menu, attention_icon, passive_icon)

        self.item.activated.connect(self.emit_triggered)

    def _create_item(self):
        self.item = QtGui.QSystemTrayIcon(self._passive_icon.icon(), self._window)
        self.item.setContextMenu(self._menu.item)
        self.item.show()

    @AIndicator.attention.setter
    def attention(self, value):
        if value:
            self.item.setIcon(self._attention_icon.icon())
        else:
            self.item.setIcon(self._passive_icon.icon())

        self._attention = value

    @AIndicator.hidden.getter
    def hidden(self):
        self._hidden = self.item.isVisible()
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        if value:
            self.item.hide()
        else:
            self.item.show()

        self._hidden = value

    @AIndicator.attention_icon.setter
    def attention_icon(self, value):
        if self.attention:
            self.item.setIcon(value.icon())

        self._attention_icon = value

    @AIndicator.passive_icon.setter
    def passive_icon(self, value):
        if not self.attention:
            self.item.setIcon(value.icon())
        self._passive_icon = value
