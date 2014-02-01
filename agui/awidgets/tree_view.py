from agui.awidgets import AWidget

class ATreeView(AWidget):
    def __init__(self, item = None):
        self._selected = None
        AWidget.__init__(self, item)

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, value):
        self._selected = value

    def add_row(self, id, data, tooltip = '', color = '', parent = None):
        raise NotImplementedError()

    def add_column(self, name):
        raise NotImplementedError()

    def clear(self):
        raise NotImplementedError()

    def expand_all(self):
        raise NotImplementedError()
