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
