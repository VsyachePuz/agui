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

from agui import Object, Signal

class AWidget(Object):
    button_left = 1
    button_middle = 2
    button_right = 3

    def __init__(self, item = None):
        self._hidden = False
        self._enabled = True
        self._context_menu = None

        Object.__init__(self)

        if item is None:
            item = self._create_item()

        self.item = item
        self.check_type()

        self.button_press = Signal()
        self.double_button_press = Signal()
        self.button_release = Signal()

    def _create_item(self):
        raise NotImplementedError('Creating a backend gui item is not yet supported') #TODO

    def check_type(self):
        if hasattr(self, 'type') and self.item.__class__.__name__ != self.type:
            raise TypeError('Type of gui widget (%s) does not match class\' type (%s)' % self.item.__class__.__name__, self.type)

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

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    @property
    def context_menu(self):
        return self._context_menu

    @context_menu.setter
    def context_menu(self, value):
        self._context_menu = value
