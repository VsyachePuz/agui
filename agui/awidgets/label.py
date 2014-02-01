from agui.awidgets import AWidget

class ALabel(AWidget):
    def __init__(self, item = None):
        self._text = ''

        AWidget.__init__(self, item)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
