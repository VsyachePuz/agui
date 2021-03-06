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

from agui.awidgets import AButton
from agui.backends.gtk.widgets import Widget

class Button(Widget, AButton):
    type = 'Button'

    def __init__(self, item = None):
        AButton.__init__(self, item)
        Widget.__init__(self, item)

        self.item.connect('button-press-event', self.emit_pressed)

    @AButton.text.getter
    def text(self):
        self._text = self.item.get_label()
        return self._text

    @text.setter
    def text(self, value):
        self.item.set_label(value)
        self._text = value

    @AButton.icon.setter
    def icon(self, value):
        self.item.set_image(value.icon())
        self._icon = value
