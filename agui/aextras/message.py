from agui import Object

class AMessage(Object):
    def message(self, window_title, title, message, icon):
        raise NotImplementedError()

    def message(self, window_title, message, icon):
        raise NotImplementedError()
