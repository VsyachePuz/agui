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
from agui.awidgets import AMenu
from agui.backends.pyside.widgets import Widget

class Menu(Widget, AMenu):
    type = 'QMenu'

    def __init__(self, item = None):
        AMenu.__init__(self, item)

        self.item.triggered(self.emit_triggered)

    def _create_item(self):
        self.item = QtGui.QMenu()
        return self.item

    def append(self, text, icon = None):
        if icon is None:
            self.item.addAction(icon.icon(), text)
        else:
            self.item.addAction(text)

    def get_text(self, widget):
        return widget.text()

    def popup(self, widget, event):
        raise NotImplementedError('Popup has not yet been implemented') #TODO
