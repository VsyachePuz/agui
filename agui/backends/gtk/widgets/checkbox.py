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

from agui.awidgets import ACheckBox
from agui.backends.gtk.widgets import Widget

class CheckBox(Widget, ACheckBox):
    type = 'Switch'

    def __init__(self, item = None):
        ACheckBox.__init__(self, item)
        Widget.__init__(self, item)

        self.item.connect('notify::active', self.emit_changed)

    @ACheckBox.checked.getter
    def checked(self):
        self._checked = self.item.get_active()
        return self._checked

    @checked.setter
    def checked(self, value):
        self.item.set_active(value)
        self._checked = value
