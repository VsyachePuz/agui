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

from agui.awidgets import AComboBox
from agui.backends.pyside.widgets import Widget

class ComboBox(Widget, AComboBox):
    type = 'QComboBox'

    def __init__(self, item = None):
        AComboBox.__init__(self, item)

        self.item.currentIndexChanged.connect(self.emit_changed)

    def clear(self):
        self.item.clear()
        AComboBox.clear(self)

    def append(self, text):
        self.item.addItem(text)
        AComboBox.append(self, text)

    def prepend(self, text):
        self.item.insertItem(0, text)
        AComboBox.prepend(self, text)

    def remove(self, index):
        self.item.removeItem(index)
        AComboBox.remove(self, index)

    def insert(self, index, text):
        self.item.insertItem(index, text)
        AComboBox.insert(self, index, text)

    @AComboBox.selected.getter
    def selected(self):
        self._selected = self.item.currentIndex()
        return self._selected

    @selected.setter
    def selected(self, value):
        self.item.setCurrentIndex(value)
        self._selected = value

    @AComboBox.selected_text.getter
    def selected_text(self):
        return self.item.currentText()
