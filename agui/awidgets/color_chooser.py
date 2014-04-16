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
from agui.helpers import functions

class AColorChooser(AWidget):
    def __init__(self, item, parent = None):
        self._color_hex = ''
        self.parent = parent
        AWidget.__init__(self, item)

    @property
    def color_hex(self):
        return self._color

    @color_hex.setter
    def color_hex(self, value):
        self._color_hex = value

    @property
    def color_rgb(self):
        return functions.hex_to_rgb(self.color_hex)

    @color_hex.setter
    def color_rgb(self, value):
        self.color_hex = functions.rgb_to_hex(value)
