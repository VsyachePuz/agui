from agui.awidgets import AWidget

class Widget(AWidget):
    def __init__(self, item = None):
        AWidget.__init__(self, item)

        self.item.connect('button-press-event', emit_button_pressed)
        self.item.connect('button-release-event', emit_button_released)
        self.item.connect('popup-menu', emit_context_menu)

    @AWidget.hidden.getter
    def hidden(self):
        self._hidden = not self.item.get_visible()
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        if value:
            self.item.hide()
        else:
            self.item.show()

        self._hidden = value

    def enable(self):
        self.item.set_sensitive(True)

    def disable(self):
        self.item.set_sensitive(False)
