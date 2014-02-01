from agui.backends.pyside.imports import *
from agui.awidgets import ATreeView
from agui.backends.pyside.widgets import Widget
from agui.helpers.functions import hex_to_rgb

class TreeView(Widget, ATreeView):
    type = 'QTreeWidget'
    _column_id = 1

    def __init__(self, item = None):
        ATreeView.__init__(self, item)

    @ATreeView.selected.getter
    def selected(self):
        selected_items = self.item.selectedItems()
        selected = selected_items[0]

        return selected.text(self._column_id)

    def add_row(self, id, data, tooltip = '', color = '', parent = None):
        data.append(id)

        row = None
        if parent is None:
            row = QtGui.QTreeWidgetItem(self.item, data)
        else:
            row = QtGui.QTreeWidgetItem(parent, data)

        color = hex_to_rgb(color)
        row_brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        row_brush.setColor(QtGui.QColor(color[0], color[1], color[2]))
        for i in range(len(data) - 1):
            row.setBackground(i, row_brush)
            if tooltip != '':
                row.setToolTip(i, tooltip)

        if parent is None:
            self.item.addTopLevelItem(row)

    def add_column(self, name):
        pass #Nothing to do here, these get setup in the ui file

    def clear(self):
        self.item.clear()

    def expand_all(self):
        self.item.expandAll()
