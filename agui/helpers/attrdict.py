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

class AttrDict(object):
    def __init__(self, **kwargs):
        self._dict = {}

        for key, value in kwargs.iteritems():
            self._dict[key] = value

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __getitem__(self, key):
        return self._dict[key]

    def __delitem__(self, key):
        del self._dict[key]

    def __setattr__(self, key, value):
        if key != '_dict':
            self._dict[key] = value
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, key):
        if key != '_dict':
            return self._dict[key]
        else:
            return object.__getattr__(self, key)

    def __delattr__(self, key):
        if key != '_dict':
            del self._dict[key]
        else:
            object.__delattr__(self, key)

    def __contains__(self, key):
        return (key in self._dict)
