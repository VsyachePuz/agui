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

from agui import Object

class AIcon(Object):
    size_button = 0
    size_menu = 1
    size_dialog = 2

    def __init__(self, name, fallback = ''): #TODO: add font awesome icons
        self._name = name
        self._fallback = fallback
        self.icon = None
        self._use_fallback = False

    def name(self):
        name = self._name
        if self._use_fallback:
            name = self._fallback

        return name

    def icon(self, size = None):
        raise NotImplementedError()
