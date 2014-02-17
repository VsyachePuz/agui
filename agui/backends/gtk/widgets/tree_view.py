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
from agui.awidgets import ATreeView
from agui.backends.gtk.widgets import Widget

class TreeView(Widget, ATreeView):
    type = 'TreeView'
    _column_id = 0
    _column_background = 1
    _column_tooltip = 2

    def __init__(self, item = None):
        ATreeView.__init__(self, item)
        Widget.__init__(self, item)

        self.tree_store_gtk = self.item.get_model()
        self.item.set_tooltip_column(self._column_tooltip)

    @ATreeView.selected.getter
    def selected(self):
        model, row = self.item.get_selection().get_selected()

        id = None
        if row is not None and model.iter_is_valid(row):
            id = model.get_value(row, 0)

        self._selected = id
        return self._selected

    def add_row(self, id, data, tooltip = '', color = '', parent = None):
        row = [id, color, tooltip]
        row.extend(data)

        return self.tree_store_gtk.append(parent, row)

    def clear(self):
        self.tree_store_gtk.clear()

    def expand_all(self):
        self.item.expand_all()
