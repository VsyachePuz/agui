from agui.awidgets import ALineEdit
from agui.backends.gtk.widgets import Widget

class LineEdit(Widget, ALineEdit):
    type = 'Entry'

    def __init__(self, item = None):
        ALineEdit.__init__(self, item)

        self.item.connect('changed', self.emit_changed)
        self.item.connect('icon-release', self._button_gtk)

    def _button_gtk(self, widget, pos, event, data = None):
        if pos == 1 and self.has_clear:
            self.clear()
        elif pos == 0 and self.has_error:
            self.focus()

    @ALineEdit.text.getter
    def text(self):
        self._text = self.item.get_text()
        return self._text

    @text.setter
    def text(self, value):
        self.item.set_text(value)
        self._text = value

    def focus(self):
        self.item.grab_focus()

    def hide_error(self):
        self._last_error_gtk = self.item.get_icon_name()
        self.item.set_icon_from_icon_name(0, None)

    def show_error(self, name = None):
        if name is not None:
            self.item.set_icon_from_icon_name(0, name)
        else:
            self.item.set_icon_from_icon_name(0, self._last_error_gtk)
