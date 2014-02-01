from agui.backends.pyside.imports import *
from agui.awidgets import AIcon

class Icon(AIcon):
    def __init__(self, name, fallback = ''):
        self._use_fallback = not QtGui.QIcon.hasThemeIcon(self.name)
        self.item = QtGui.QIcon.fromTheme(self.name, QtGui.QIcon(self.fallback))

    def icon(self, size = None):
        return self.item
