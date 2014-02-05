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
