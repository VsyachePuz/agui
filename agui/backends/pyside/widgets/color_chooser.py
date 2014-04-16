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

from agui.backends.pyside.imports import *
from agui.awidgets import AColorChooser
from agui.backends.pyside.widgets import Widget

class ColorChooser(Widget, AColorChooser):
    promote_type = 'QPushButton'

    def __init__(self, item, parent = None):
        AColorChooser.__init__(self, item, parent)
        Widget.__init__(self, item)

        self.item.pressed.connect(self._popup_chooser)
        self._update_button()

    @AColorChooser.color_hex.setter
    def color_hex(self, value):
        self._color_hex = value
        self._update_button()

    def _popup_chooser(self):
        old_color = self.color_rgb
        old_color = QColor.fromRgb(old_color[0], old_color[1], old_color[2])

        parent = None
        if self.parent is not None:
            parent = self.parent.item

        self.color_rgb = QtGui.QColorDialog.getColor(old_color, parent).getRgb()
        self._update_button()

    def _update_button(self):
        self.item.setStyleSheet("QPushButton { color:rgb(%d, %d, %d) }" % self.color_rgb)
        self.item.setText("(%d, %d, %d)" % self.color_rgb)
