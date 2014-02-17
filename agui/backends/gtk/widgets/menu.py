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

from agui.backends.gtk.imports import *
from agui.awidgets import AMenu
from agui.backends.gtk.widgets import Widget

class Menu(Widget, AMenu):
    type = 'Menu'

    def __init__(self, item = None):
        AMenu.__init__(self, item)
        Widget.__init__(self, item)

    def _create_item(self):
        self.item = Gtk.Menu()
        return self.item

    def append(self, text, icon = None):
        menu_item = None
        if icon is None:
            menu_item = Gtk.ImageMenuItem()
            menu_item.set_use_stock(False)
            menu_item.set_image(self.icon.icon())
        else:
            menu_item = Gtk.MenuItem()

        menu_item.set_label(text)
        menu_item.connect('activate', self.emit_triggered)
        menu_item.show()
        self.item.append(menu_item)

    def get_text(self, widget):
        return widget.get_label()

    def popup(self, widget, event):
        self.item.popup(None, None, None, None, event.button, event.time)
