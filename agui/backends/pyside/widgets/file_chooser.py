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

from agui import APP
from agui.backends.pyside.imports import *
from agui.awidgets import AFileChooser
from agui.backends.pyside.widgets import Widget

class FileChooser(Widget, AFileChooser):
    promote_type = 'QPushButton'
    promote_type_alt = 'QToolButton'

    def __init__(self, item, parent=None):
        AFileChooser.__init__(self, item, parent)
        Widget.__init__(self, item)

        self._types = []

        self.clear()
        self.item.pressed.connect(self._popup_chooser)

    def add_type(self, type):
        self._types.append(type)

    def clear(self):
        self.file = ''
        self.item.setText(APP.tr('(None)'))

    def _popup_chooser(self):
        filter = ''
        for type in self._types:
            if filter == '':
                filter = type
            else:
                filter = '%s %s' % (filter, type)

        filter = '(%s)' % (filter)

        parent = None
        if self.parent is not None:
            parent = self.parent.item

        (filename, selected_filter) = QtGui.QFileDialog.getOpenFileName(parent, self._title, self._dir, filter)#TODO: parent?
        self.file = filename
