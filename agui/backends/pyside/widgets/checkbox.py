from agui.awidgets import ACheckBox
from agui.backends.pyside.widgets import Widget

class CheckBox(Widget, ACheckBox):
    type = 'QCheckBox'

    def __init__(self, item = None):
        ACheckBox.__init__(self, item)

        self.item.stateChanged.connect(self.emit_changed)

    @ACheckBox.checked.getter
    def checked(self):
        self._checked = self.item.isChecked()
        return self._checked

    @checked.setter
    def checked(self, value):
        self.item.setChecked(value)
        self._checked = value
