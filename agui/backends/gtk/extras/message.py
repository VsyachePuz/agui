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

from agui.aextras import AMessage
from agui.backends.gtk.imports import *

class Message(AMessage):
    def _destroy(self, widget, *args):
        widget.destroy()

    def message(self, window_title, title, message, icon, parent=None):
        dialog = Gtk.MessageDialog(parent, Gtk.DialogFlags.MODAL,
            Gtk.MessageType.INFO, Gtk.ButtonsType.OK, title)
        dialog.set_image(icon.icon(icon.size_dialog))
        dialog.set_title(window_title)
        dialog.format_secondary_text(message)

        dialog.connect('response', self._destroy)
        dialog.show()

    def message_alt(self, window_title, message, icon, parent=None):
        dialog = Gtk.MessageDialog(parent, Gtk.DialogFlags.MODAL,
            Gtk.MessageType.INFO, Gtk.ButtonsType.OK, message)
        dialog.set_image(icon.icon(icon.size_dialog))
        dialog.set_title(window_title)

        dialog.connect('response', self._destroy)
        dialog.show()

    def yes_no(self, window_title, message, parent=None):
        dialog = Gtk.MessageDialog(parent, Gtk.DialogFlags.MODAL,
            Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, message)
        dialog.set_title(window_title)

        ans = dialog.run()
        dialog.destroy()

        value = self.no
        if ans == -8:
            value = self.yes

        return value
