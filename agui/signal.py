from agui import APP, Object

def slot(func):
    if APP.is_pyside():
        func = QtCore.Slot(func)

    return func

class Signal(Object):
    def __init__(self):
        self.slots = []

    def connect(self, slot):
        self.slots.append(slot)

    @slot
    def emit(self, *args):
        for slot in self.slots:
            slot(*args)
