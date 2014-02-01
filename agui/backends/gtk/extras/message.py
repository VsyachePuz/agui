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
    def message(self, window_title, title, message, icon):
        dialog = Gtk.MessageDialog(flags=Gtk.DialogFlags.MODAL, message_format=title)
        dialog.set_image(icon.icon(icon.size_dialog))
        dialog.set_title(window_title)
        dialog.format_secondary_text(message)
        dialog.show()

    def message(self, window_title, message, icon):
        dialog = Gtk.MessageDialog(flags=Gtk.DialogFlags.MODAL, message_format=message)
        dialog.set_image(icon.icon(icon.size_dialog))
        dialog.set_title(window_title)
        dialog.show()
