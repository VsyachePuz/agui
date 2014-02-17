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
from agui.awidgets import AWidget

class Widget(AWidget):
    def __init__(self, item = None):
        #AWidget.__init__(self, item)

        self.item.connect('button-release-event', self._button_handler)
        self.item.connect('button-press-event', self._button_handler)

    def _button_handler(self, widget, event):
        if event.type == Gdk.EventType.BUTTON_PRESS:
            self.button_press.emit(event.button, event.x, event.y)

            if self._context_menu is not None and event.button == self.button_right:
                self._context_menu.popup(widget, event)

        elif event.type == Gdk.EventType.DOUBLE_BUTTON_PRESS:
            self.double_button_press.emit(event.button, event.x, event.y)
        elif event.type == Gdk.EventType.BUTTON_RELEASE:
            self.button_release.emit(event.button, event.x, event.y)

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

    @AWidget.enabled.getter
    def enabled(self):
        self._enabled = self.get_sensitive()
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self.item.set_sensitive(value)
        self._enabled = value
