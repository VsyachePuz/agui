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

from agui import Signal
from agui.awidgets import AWidget

class AMenu(AWidget):
    def __init__(self, item = None):
        self.triggered = Signal()

        AWidget.__init__(self, item)

    def emit_triggered(self, *args):
        self.triggered.emit(self.get_text(*args))

    def append(self, text, icon = None):
        raise NotImplementedError()

    def get_text(self, widget):
        raise NotImplementedError()

    def popup(self, *args):
        raise NotImplementedError()
