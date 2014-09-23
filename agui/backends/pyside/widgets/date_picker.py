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
from agui.awidgets import ADatePicker
from agui.backends.pyside.widgets import Widget

class DatePicker(Widget, ADatePicker):
    type = 'QDateEdit'
    format = 'MM/dd/yy'

    def __init__(self, item = None):
        ADatePicker.__init__(self, item)
        Widget.__init__(self, item)

        self.item.dateChanged.connect(self.emit_changed)

    @ADatePicker.date.getter
    def date(self):
        self._time = self.item.date().toString(self.format)
        return self._time

    @date.setter
    def date(self, value):
        date = QtCore.QDate()
        if value is not None:
            date = QtCore.QDate.fromString(value, self.format)

        self.item.setDate(date)
        self._date = value
