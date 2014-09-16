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
    def emit_closed(self, *args):
        self.closed.emit()

    def __init__(self, name, file, parent=None):#TODO pass signal handlers
        Object.__init__(self)

        self.file = file
        self.name = name
        self.parent = parent

        self._builder = None
        self._hidden = False
        self._title = ''

        self.item = None
        self.widgets = AttrDict()
        self.other_widgets = AttrDict()

        self.classes = find_classes(agui.widgets)

        self.closed = Signal()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

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

    def resize(self, width, height):
        raise NotImplementedError()

    def promote(self, name, clss):
        widget = None
        if name in self.widgets:
            widget = self.widgets[name].item
            del self.widgets[name]
        elif name in self.other_widgets:
            widget = self.other_widgets[name]
            del self.other_widgets[name]
        else:
            raise KeyError('%s not a widget in this window' % (name))

        if not hasattr(clss, 'promote_type'):
            raise TypeError('cannot promote to %s' % (clss.__class__.__name__))

        if widget.__class__.__name__ != clss.promote_type:
            raise_error = True
            if hasattr(clss, 'promote_type_alt'):
                if widget.__class__.__name__ != clss.promote_type_alt:
                    raise TypeError('widget is not of type %s, it is %s' % (widget.__class__.__name__, clss.promote_type_alt))
                else:
                    raise_error = False

            if raise_error:
                raise TypeError('widget is not of type %s, it is %s' % (widget.__class__.__name__, clss.promote_type))

        self.widgets[name] = clss(widget, self)
