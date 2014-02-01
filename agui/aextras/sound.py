from agui import Object

class ASound(Object):
    def __init__(self, filename, times_to_play = 1):
        self.filename = filename
        self.times_to_play = times_to_play

    def play(self, length = 0):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()
