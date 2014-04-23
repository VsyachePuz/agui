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

from agui.awidgets import ALineEdit
from agui.backends.gtk.widgets import Widget

class LineEdit(Widget, ALineEdit):
    type = 'Entry'

    def __init__(self, item = None):
        ALineEdit.__init__(self, item)
        Widget.__init__(self, item)

        self.item.connect('changed', self.emit_changed)
        self.item.connect('icon-release', self._button_gtk)

        self._last_error_gtk = None

    @ALineEdit.has_error.setter
    def has_error(self, value):
        self._has_error = value

        if self._has_error:
            self._last_error_gtk = self.item.get_icon_name(0)

    def _button_gtk(self, widget, pos, event, data = None):
        if pos == 1 and self.has_clear:
            self.clear()
        elif pos == 0 and self.has_error:
            self.focus()

    @ALineEdit.text.getter
    def text(self):
        self._text = self.item.get_text()
        return self._text

    @text.setter
    def text(self, value):
        self.item.set_text(value)
        self._text = value

    def focus(self):
        self.item.grab_focus()

    def hide_error(self):
        self.item.set_icon_from_icon_name(0, None)

    def show_error(self, name = None):
        if name is not None:
            self._last_error_gtk = name
            self.item.set_icon_from_icon_name(0, name)
        else:
            self.item.set_icon_from_icon_name(0, self._last_error_gtk)

    def insert_at_cursor(self, text):
        buffer = self.item.get_buffer()
        pos = self.item.get_position()
        buffer.insert_text(pos, text, -1)
