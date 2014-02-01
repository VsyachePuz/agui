from agui.awidgets import ATextArea
from agui.backends.pyside.widgets import Widget

class TextArea(Widget, ATextArea):
    type = 'QPlainTextEdit'

    def __init__(self, item = None):
        ATextArea.__init__(self, item)

        self.item.textChanged.connect(self.emit_changed)

    @ATextArea.text.getter
    def text(self):
        self._text = self.item.document().toPlainText()
        return self._text

    @text.setter
    def text(self, value):
        self.item.setPlainText(value)
        self._text = value

    def insert(self, text):
        self.item.insertPlainText(text)
        self._text = self.text
