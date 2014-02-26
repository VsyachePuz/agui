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

from agui.aextras import AIcon
from agui.backends.gtk.imports import *

class Icon(AIcon):
    def __init__(self, name, fallback = ''):
        AIcon.__init__(self, name, fallback)

        self._use_fallback = not Gtk.IconTheme().get_default().has_icon(name)

    def icon(self, size = None):
        self.item = Gtk.Image()

        if self._use_fallback:
            self.item.set_from_file(self._fallback)
        else:
            size2 = Gtk.IconSize.BUTTON
            if size == self.size_menu:
                size2 = Gtk.IconSize.MENU
            elif size == self.size_dialog:
                size2 = Gtk.IconSize.DIALOG

            self.item.set_from_icon_name(self._name, size2)

        self.item.show()
        return self.item

    def _gicon(self):
        self._gitem = None

        if self._use_fallback:
            self._gitem = Gio.FileIcon(Gio.File(self.fallback))
        else:
            self._gitem = Gio.ThemedIcon(self._name)

        return self._gitem
