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

from agui.awidgets import AFileChooser
from agui.backends.gtk.widgets import Widget

class FileChooser(Widget, AFileChooser):
    promote_type = 'FileChooserButton'

    def __init__(self, item):
        AFileChooser.__init__(self, item)
        Widget.__init__(self, item)

    @AFileChooser.file.getter
    def file(self):
        self._file = self.item.get_filename()
        return self._file

    @file.setter
    def file(self, value):
        self.item.set_filename(value)
        self._file = value

    @AFileChooser.dir.getter
    def dir(self):
        self._dir = self.item.get_current_folder()
        return self._dir

    @dir.setter
    def dir(self, value):
        self.item.set_current_folder(value)
        self._dir = value

    @AFileChooser.title.getter
    def title(self):
        self._title = self.item.get_title()
        return self._title

    @title.setter
    def title(self, value):
        self.item.set_title(value)
        self._title = value

    def add_type(self, type):
        self.item.get_file().add_pattern(type)

    def clear(self):
        self.item.unselect_all()
