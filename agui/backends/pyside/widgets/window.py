from agui.backends.pyside.imports import *
from agui.awidgets import AWindow
from agui.helpers import AttrDict
from xml.etree.cElementTree import ElementTree

class Window(AWindow):
    def __init__(self, type, name, file):
        AWindow.__init__(self, type, name, file)
        self._ok_to_close = False

        self.builder = QtUiTools.QUiLoader()
        self.item = self.builder.load(self.file)

        self._types = {}
        for cls in self.classes:
            if hasattr(cls, 'type'):
                self._types[cls.type] = cls

        for child in self._find_children():
            name = child.objectName()
            type = child.__class__.__name__

            if type in self._types:
                self.widgets[name] = self._types[type](child)
            else:
                self.other_widgets[name] = AttrDict(widget=child, type=type)

        self.item.closeEvent = self._build_close_event()

    def _build_close_event(self):
        agui_window = self

        def closeEvent(self, event):
            agui_window.emit_closed()
            if agui_window._ok_to_close:
                event.accept()
            else:
                event.ignore()

        return closeEvent

    def _find_children(self, parent = None):
        children = []
        if parent is None:
            parent = self.item

        for child in parent.children():
            if child.objectName() != '':
                children.append(child)
                children.extend(self._find_children(child))

        return children

    @property
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

    def close(self):
        self._ok_to_close = True
        self.item.close()

    def replace(self, old, new):
        raise NotImplementedError('replace has not yet been implemented') #TODO
