from agui import Object

class AIcon(Object):
    size_button = 0
    size_menu = 1
    size_dialog = 2

    def __init__(self, name, fallback = ''): #TODO: add font awesome icons
        self._name = name
        self._fallback = fallback
        self.icon = None
        self._use_fallback = False

    def name(self):
        name = self._name
        if self._use_fallback:
            name = self._fallback

        return name

    def icon(self, size = None):
        raise NotImplementedError()
