# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2014 Brian Douglass bhdouglass@gmail.com
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

from agui.backends.gtk.imports import *
from agui.awidgets import AWindow
from agui.helpers import AttrDict
from xml.etree.cElementTree import ElementTree

class Window(AWindow):
    def __init__(self, name, file, parent=None):
        AWindow.__init__(self, name, file, parent)

        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.file)
        self.item = self.builder.get_object(self.name)
        if self.parent is not None:
            self.item.set_transient_for(self.parent.item)

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
                self.other_widgets[name] = widget

        self.item.connect('delete-event', self.emit_closed)

    @AWindow.title.getter
    def title(self):
        self._title = self.item.get_title()
        return self._title

    @title.setter
    def title(self, value):
        self.item.set_title(value)
        self._title = value

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

    def resize(self, width, height):
        self.item.resize(width, height)
