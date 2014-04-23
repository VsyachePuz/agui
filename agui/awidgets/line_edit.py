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

class ALineEdit(AWidget):
    def __init__(self, item = None):
        self._has_clear = False
        self._has_error = False
        self._text = ''
        self.changed = Signal()

        AWidget.__init__(self, item)

    def emit_changed(self, *args):
        self.changed.emit(self.text)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def clear(self):
        self.text = ''

    @property
    def has_clear(self):
        return self._has_clear

    @has_clear.setter
    def has_clear(self, value):
        self._has_clear = value

    @property
    def has_error(self):
        return self._has_error

    @has_error.setter
    def has_error(self, value):
        self._has_error = value

    def focus(self):
        raise NotImplementedError()

    def hide_error(self):
        raise NotImplementedError()

    def show_error(self, name = None):
        raise NotImplementedError()

    def insert_at_cursor(self, text):
        raise NotImplementedError()
