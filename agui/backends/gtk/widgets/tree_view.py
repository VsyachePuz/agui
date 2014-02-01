from agui.backends.gtk.imports import *
from agui.awidgets import ATreeView
from agui.backends.gtk.widgets import Widget

class TreeView(Widget, ATreeView):
    type = 'TreeView'
    _column_id = 0
    _column_background = 1
    _column_tooltip = 2
    _column_start = 2

    def __init__(self, item = None):
        ATreeView.__init__(self, item)

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

    def add_column(self, name):
        cell = Gtk.CellRendererText()
        cell.set_property('background-set' , True)

        self._column_start += 1
        col = Gtk.TreeViewColumn(name, cell, text=self._column_start, background=1)
        col.set_min_width(10)
        col.set_resizable(True)
        col.set_spacing(0)
        self.item.append_column(col)

    def clear(self):
        self.tree_store_gtk.clear()

    def expand_all(self):
        self.item.expand_all()
