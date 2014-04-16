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
from agui.awidgets import AColorChooser
from agui.backends.gtk.widgets import Widget

class ColorChooser(Widget, AColorChooser):
    promote_type = 'ColorButton'

    def __init__(self, item, parent = None):
        AColorChooser.__init__(self, item, parent)
        Widget.__init__(self, item)

    @AColorChooser.color_hex.getter
    def color_hex(self):
        self._color_hex = self.item.get_color().to_string()
        return self._color_hex

    @color_hex.setter
    def color_hex(self, value):
        self.item.set_color(Gdk.color_parse(value))
        self._color_hex = value
