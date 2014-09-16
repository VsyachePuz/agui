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

class ATimeout(Object):
    def __init__(self, seconds, function, *args):
        self.item = None
        self.seconds = seconds
        self.function = function
        self.args = args

    def _function(self):
        self.function(*self.args)

    def started(self):
        return (self.item is not None)

    def start(self):
        if self.started():
            raise RuntimeError('Cannot start a timeout that is already started')

    def stop(self):
        if not self.started():
            raise RuntimeError('Cannot stop a timeout that has not been started')
