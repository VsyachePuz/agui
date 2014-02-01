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

from agui import Signal
from agui.awidgets import AWidget

class AComboBox(AWidget):
    def __init__(self, item = None):
        self._list = []
        self._selected = 0
        self.changed = Signal()

        AWidget.__init__(self, item)

    def emit_changed(self, *args):
        self.changed.emit(self.selected)

    def clear(self):
        self._list = []

    def append(self, text):
        self._list.append(text)

    def prepend(self, text):
        self._list.insert(0, text)

    def remove(self, index):
        self._list.remove(index)

    def insert(self, index, text):
        self._list.insert(index, text)

    @property
    def items(self):
        return self._list

    @items.setter
    def items(self, items):
        self.clear()
        for item in items:
            self.append(item)

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, value):
        self._selected = value

    @property
    def selected_text(self):
        return self._list[self.selected]

    @selected_text.setter
    def selected_text(self, value):
        index = 0
        for item in self._list:
            if text == item:
                self.selected = index
                break

            index += 1
