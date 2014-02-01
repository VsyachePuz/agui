from agui.awidgets import ALineEdit
from agui.backends.pyside.widgets import Widget

class LineEdit(Widget, ALineEdit):
    type = 'QLineEdit'

    def __init__(self, item = None):
        ALineEdit.__init__(self, item)

        self.item.textChanged.connect(self.emit_changed)
        #TODO: has_clear & has_error

    @ALineEdit.text.getter
    def text(self):
        self._text = self.item.text()
        return self._text

    @text.setter
    def text(self, value):
        self.item.setText(value)
        self._text = value

    def focus(self):
        self.item.setFocus()

    def hide_error(self):
        raise NotImplementedError('hide_error has not yet been implemented') #TODO

    def show_error(self, name = None):
        raise NotImplementedError('show_error has not yet been implemented') #TODO
