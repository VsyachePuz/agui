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

from agui.awidgets import AWidget

class Widget(AWidget):
    def __init__(self, item = None):
        AWidget.__init__(self, item)

        self.item.connect('button-press-event', emit_button_pressed)
        self.item.connect('button-release-event', emit_button_released)
        self.item.connect('popup-menu', emit_context_menu)

    @AWidget.hidden.getter
    def hidden(self):
        self._hidden = not self.item.get_visible()
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        if value:
            self.item.hide()
        else:
            self.item.show()

        self._hidden = value

    def enable(self):
        self.item.set_sensitive(True)

    def disable(self):
        self.item.set_sensitive(False)
