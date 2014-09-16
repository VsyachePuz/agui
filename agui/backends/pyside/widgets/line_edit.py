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
from agui.awidgets import ALineEdit
from agui.backends.pyside.widgets import Widget

class LineEdit(Widget, ALineEdit):
    type = 'QLineEdit'

    def __init__(self, item = None):
        ALineEdit.__init__(self, item)
        Widget.__init__(self, item)

        self.item.textChanged.connect(self.emit_changed)

    @ALineEdit.has_error.setter
    def has_error(self, value):
        self._has_error = value

        self._error_button = None
        if self._has_error:
            name = '%s_error_button' % self.item.objectName()
            self._error_button = self.item.parent().findChild(QtGui.QPushButton, name)
            if self._error_button is None:
                self._error_button = self.item.parent().findChild(QtGui.QToolButton, name)

                if self._error_button is None:
                    raise IndexError('Could not find button named "%s"' % name)

    @ALineEdit.has_clear.setter
    def has_clear(self, value):
        self._has_clear = value

        self._clear_button = None
        if self._has_clear:
            name = '%s_clear_button' % self.item.objectName()
            self._clear_button = self.item.parent().findChild(QtGui.QPushButton, name)
            if self._clear_button is None:
                self._clear_button = self.item.parent().findChild(QtGui.QToolButton, name)

            if self._clear_button is not None:
                self._clear_button.pressed.connect(self.clear)

    @ALineEdit.text.getter
    def text(self):
        self._text = self.item.text()
        return self._text

    @text.setter
    def text(self, value):
        self.item.setText(value)
        self._text = value

    def focus(self):
        self.item.setFocus()

    def hide_error(self):
        if self._has_error and self._error_button is not None:
            self._error_button.hide()

    def show_error(self, name = None):#TODO: name
        if self._has_error and self._error_button is not None:
            self._error_button.show()

    def insert_at_cursor(self, text):
        self.item.insert(text)
