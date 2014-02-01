from agui.backends.gtk.imports import *
from agui.awidgets import AWindow
from agui.helpers import AttrDict
from xml.etree.cElementTree import ElementTree

class Window(AWindow):
    def __init__(self, type, name, file):
        AWindow.__init__(self, type, name, file)

        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.file)
        self.item = self.builder.get_object(self.name)

        self.types = {}
        for cls in self.classes:
            if hasattr(cls, 'type'):
                self.types[cls.type] = cls

        tree = ElementTree()
        tree.parse(self.file)
        ele_widgets = tree.getiterator("object")
        for ele_widget in ele_widgets:
            name = ele_widget.attrib['id']
            widget = self.builder.get_object(name)
            type = widget.__class__.__name__

            if type in self.types:
                self.widgets[name] = self.types[type](widget)
            else:
                self.other_widgets[name] = AttrDict(widget=widget, type=type)

        self.item.connect('delete-event', self.emit_closed)

    @AWindow.hidden.getter
    def hidden(self):
        self._hidden = self.item.get_visible()
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        if value:
            self.item.hide()
        else:
            self.item.show()

        self._hidden = value

    def close(self):
        self.item.destroy()

    def replace(self, old, new):
        parent = old.get_parent()
        if not parent:
            raise RuntimeError('No parent for old widget')

        parent.remove(old)
        parent.add(new)
