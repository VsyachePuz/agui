from agui.awidgets import ACheckBox
from agui.backends.gtk.widgets import Widget

class CheckBox(Widget, ACheckBox):
    type = 'Switch'

    def __init__(self, item = None):
        ACheckBox.__init__(self, item)

        self.item.connect('notify::active', self.emit_changed)

    @ACheckBox.checked.getter
    def checked(self):
        self._checked = self.item.get_active()
        return self._checked

    @checked.setter
    def checked(self, value):
        self.item.set_active(value)
        self._checked = value
