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

from agui.awidgets import ALineEdit
from agui.backends.pyside.widgets import Widget

class LineEdit(Widget, ALineEdit):
    type = 'QLineEdit'

    def __init__(self, item = None):
        ALineEdit.__init__(self, item)
        Widget.__init__(self, item)

        self.item.textChanged.connect(self.emit_changed)
        #TODO: has_clear & has_error

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
        raise NotImplementedError('hide_error has not yet been implemented') #TODO

    def show_error(self, name = None):
        raise NotImplementedError('show_error has not yet been implemented') #TODO
