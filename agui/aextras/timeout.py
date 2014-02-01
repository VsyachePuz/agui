from agui import Object

class ATimeout(Object):
    def __init__(self, seconds, function):
        self.item = None
        self.seconds = seconds
        self.function = function

    def start(self):
        if self.item is not None:
            raise RuntimeError('Cannot start a timeout that is already started')

    def stop(self):
        if self.item is None:
            raise RuntimeError('Cannot stop a timeout that has not been started')
