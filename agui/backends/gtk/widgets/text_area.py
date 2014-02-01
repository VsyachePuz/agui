from agui.awidgets import ATextArea
from agui.backends.gtk.widgets import Widget

class TextArea(Widget, ATextArea):
    type = 'TextView'

    def __init__(self, item = None):
        ATextArea.__init__(self, item)

        self.item.connect('key-release-event', self.emit_changed)

    @ATextArea.text.getter
    def text(self):
        buffer = self.item.get_buffer()
        self._text = buffer.get_text(buffer.get_start_iter(), buffer.get_end_iter(), True)
        return self._text

    @text.setter
    def text(self, value):
        self.item.get_buffer().set_text(value)
        self._text = value

    def insert(self, text):
        self.item.insert_at_cursor(text)
        self._text = self.text
