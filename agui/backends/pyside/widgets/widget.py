from agui.awidgets import AWidget

class Widget(AWidget):
    def __init__(self, item = None):
        AWidget.__init__(self, item)

        def mousePressEvent(widget, event):
            self.emit_button_pressed(event)
            event.accept()

        def mouseReleaseEvent(widget, event):
            self.emit_button_released(event)
            event.accept()

        def contextMenuEvent(widget, event):
            self.emit_context_menu(event)
            event.accept()

        self.item.mousePressEvent = mousePressEvent
        self.item.mouseReleaseEvent = mouseReleaeeEvent
        self.item.contextMenuEvent = contextMenuEvent

    @AWidget.hidden.getter
    def hidden(self):
        self._hidden = self.item.isHidden()
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        if value:
            self.item.hide()
        else:
            self.item.show()

        self._hidden = value

    def enable(self):
        self.item.enable()

    def disable(self):
        self.item.disable()
