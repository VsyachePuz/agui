from agui.backends.pyside.imports import *
from agui.awidgets import AMenu
from agui.backends.pyside.widgets import Widget

class Menu(Widget, AMenu):
    def __init__(self):
        AMenu.__init__(self)

        self.item.triggered(self.emit_triggered)

    def _create_item(self):
        self.item = QtGui.QMenu()

    def append(self, text, icon = None):
        if icon is None:
            self.item.addAction(icon.icon(), text)
        else:
            self.item.addAction(text)

    def get_text(self, widget):
        return widget.text()

    def popup(self, widget, event):
        raise NotImplementedError('Popup has not yet been implemented') #TODO
