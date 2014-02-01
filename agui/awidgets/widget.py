from agui import Object, Signal

class AWidget(Object):
    def __init__(self, item = None):
        self._hidden = False

        Object.__init__(self)

        if item is None:
            raise NotImplementedError('Creating a backend gui item is not yet supported') #TODO

        self.item = item
        self.check_type()

        self.button_press = Signal()
        self.button_release = Signal()
        self.context_menu = Signal()

    def emit_button_pressed(self, *args):
        self.button_pressed.emit(*args)

    def emit_button_released(self, *args):
        self.button_released.emit(*args)

    def emit_context_menu(self, *args):
        self.context_menu.emit(*args)

    def check_type(self):
        if hasattr(self, 'type') and self.item.__class__.__name__ != self.type:
            raise TypeError('Type of gui widget (%s) does not match class\' type (%s)' % self.item.__class__.__name__, self.type)

    @property
    def hidden(self):
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        self._hidden = value

    def hide(self):
        self.hidden = True

    def show(self):
        self.hidden = False

    def enable(self):
        raise NotImplementedError()

    def disable(self):
        raise NotImplementedError()

#TODO: more stuff like right click?
