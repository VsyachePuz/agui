# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2014 Brian Douglass bhdouglass@gmail.com
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

from agui.aextras import ASound
from agui.backends.gtk.imports import *
from agui.backends.gtk.extras.timeout import Timeout

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
