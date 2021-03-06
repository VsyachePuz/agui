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

from agui.backends.pyside.imports import *
from agui.aextras import AMessage

class Message(AMessage):
    def message(self, window_title, title, message, icon, parent=None):
        message2 = "<b>%s</b><br/><br/>%s" % (title, message)
        self.message_alt(window_title, message2, icon, parent)

    def message_alt(self, window_title, message, icon, parent=None):
        self.dialog = QtGui.QMessageBox(None, window_title, message, QtGui.QMessageBox.Close, parent=parent)
        self.dialog.setPixmap(icon.icon().pixmap(32, 32))
        self.dialog.show()

    def yes_no(self, window_title, message, icon=None, parent=None):
        ans = QtGui.QMessageBox.question(self, window_title, message, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes, parent=parent)

        value = self.no
        if ans == QtGui.MessageBox.Yes:
            value = self.yes

        return value
