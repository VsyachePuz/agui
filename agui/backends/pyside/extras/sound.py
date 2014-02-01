from agui.awidgets import ASound
from agui.backends.pyside.imports import *
from agui.backends.pyside.extras import Timeout

class Sound(ASound):
    def __init__(self, filename, times_to_play = 1):
        ASound.__init__(self, filename, times_to_play)

    def play(self, length = 0):
        self.item = Phonon.createPlayer(Phonon.MusicCategory, Phonon.MediaSource(self.filename))

        if self.times_to_play > 0:
            for i in range(self.times_to_play - 1):
                self.item.enqueue(Phonon.MediaSource(self.filename))

        self.item.play()

        if self.length > 0:
            self._timeout = Timeout(self.length, self.stop)
            self._timeout.start()

    def stop(self):
        self.item.stop()
