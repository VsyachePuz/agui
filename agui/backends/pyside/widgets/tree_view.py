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
from agui.awidgets import ATreeView
from agui.backends.pyside.widgets import Widget
from agui.helpers.functions import hex_to_rgb

class TreeView(Widget, ATreeView):
    type = 'QTreeWidget'

    def __init__(self, item = None):
        ATreeView.__init__(self, item)
        Widget.__init__(self, item)

        self._column_id = item.columnCount() + 1
        self._rows = {}

    @ATreeView.selected.getter
    def selected(self):
        selected_items = self.item.selectedItems()
        selected = selected_items[0]
        id = None
        for sid, row in self._rows.items():
            if row is selected:
                id = int(sid)

        return id

    def add_row(self, id, data, tooltip = '', color = '', parent = None):
        row = None
        if parent is None:
            row = QtGui.QTreeWidgetItem(self.item, data)
        else:
            row = QtGui.QTreeWidgetItem(parent, data)

        row_brush = None
        if color != '':
            color = hex_to_rgb(color)
            row_brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
            row_brush.setColor(QtGui.QColor(color[0], color[1], color[2]))

        for i in range(len(data)):
            if color != '':
                row.setBackground(i, row_brush)

            if tooltip != '':
                row.setToolTip(i, tooltip)

        if parent is None:
            self.item.addTopLevelItem(row)

        self._rows[str(id)] = row
        return row

    def clear(self):
        self.item.clear()

    def expand_all(self):
        self.item.expandAll()

    def column_width(self, column, width):
        self.item.setColumnWidth(column, width)
