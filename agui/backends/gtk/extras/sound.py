from agui.awidgets import ASound
from agui.backends.gtk.imports import *
from agui.backends.gtk.extras import Timeout

class Sound(ASound):
    def __init__(self, filename, times_to_play = 1):
        ASound.__init__(self, filename, times_to_play)

        playbin = 'playbin2'
        gst_version = Gst.version()
        if gst_version[0] > 0:
            playbin = 'playbin' #gst version 1.0's playbin is gst version 0.10's playbin2

        self.player = Gst.ElementFactory.make(playbin, 'player')

    def play(self, length = 0):
        self.player.set_state(Gst.State.READY)
        self._filename = 'file://%s' % (self.filename)
        self.player.set_property('uri', self._filename)
        self.player.set_state(Gst.State.PLAYING)
        self._count = 0

        if self.times_to_play:
            self.player.connect('about-to-finish', self._about_to_finish)

        if length > 0:
            self._timeout = Timeout(length, self.stop)
            self._timeout.start()

    def stop(self):
        self.player.set_state(Gst.State.READY)

    def _about_to_finish(self):
        self._count += 1
        if self._count < self.times_to_play:
            self.player.set_property('uri', self._filename)
