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
from agui.backends.gtk.widgets import Widget

class ComboBox(Widget, AComboBox):
    type = 'ComboBoxText'

    def __init__(self, item = None):
        AComboBox.__init__(self, item)

        self.item.connect('changed', self.emit_changed)

    def clear(self):
        self.item.get_model().clear()
        AComboBox.clear(self)

    def append(self, text):
        self.item.append_text(text)
        AComboBox.append(self, text)

    def prepend(self, text):
        self.item.prepend_text(text)
        AComboBox.prepend(self, text)

    def remove(self, index):
        self.item.remove(index)
        AComboBox.remove(self, index)

    def insert(self, index, text):
        self.item.insert_text(index, text)
        AComboBox.insert(self, index, text)

    @AComboBox.selected.getter
    def selected(self):
        self._selected = self.item.get_active()
        return self._selected

    @selected.setter
    def selected(self, value):
        self.item.set_active(value)
        self._selected = value

    @AComboBox.selected_text.getter
    def selected_text(self):
        return self.item.get_active_text()
