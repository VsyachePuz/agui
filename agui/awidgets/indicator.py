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

class AIndicator(AWidget):
    def __init__(self, window, name, menu, attention_icon, passive_icon):
        self._window = window
        self._name = name
        self._menu = menu
        self._attention = False
        self._hidden = False
        self._attention_icon = attention_icon
        self._passive_icon = passive_icon

        self.triggered = Signal()

        AWidget.__init__(self, self._create_item)

    def _create_item(self):
        raise NotImplementedError()

    def emit_triggered(self, *arg):
        self.triggered.emit()

    @property
    def attention(self):
        return self._attention

    @attention.setter
    def attention(self, value):
        self._attention = value

    @property
    def hidden(self):
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        self._hidden = value

    def hide(self):
        self.hidden = True

    def show(self):
        self.hidden = False

    @property
    def attention_icon(self):
        return self._attention_icon

    @attention_icon.setter
    def attention_icon(self, value):
        self._attention_icon = value

    @property
    def passive_icon(self):
        return self._passive_icon

    @passive_icon.setter
    def passive_icon(self, value):
        self._passive_icon = value
