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

import agui.widgets
from agui import Object, Signal
from agui.helpers import AttrDict
from agui.helpers.functions import find_classes

class AWindow(Object):
    MAIN_WINDOW = 'main_window'
    DIALOG = 'dialog'

    def emit_closed(self, *args):
        self.closed.emit()

    def __init__(self, type, name, file):#TODO pass signal handlers
        Object.__init__(self)

        self.file = file
        self.name = name
        self.type = type

        self._builder = None
        self._hidden = False

        self.item = None
        self.widgets = AttrDict()
        self.other_widgets = AttrDict()

        self.classes = find_classes(agui.widgets)

        self.closed = Signal()

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

    def close(self):
        raise NotImplementedError()

    def replace(self, old, new):
        raise NotImplementedError()

    def chooser(self, name, chooser_class):
        button = self.widgets[name]
        if button.__class__.__name__ != 'Button':
            raise TypeError('%s is not a button' % name)

        chooser = chooser_class()
        self.replace(button, chooser)
        self.widgets[name] = chooser
