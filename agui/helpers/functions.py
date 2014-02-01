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

import inspect

def find_classes(module):
    return [
        cls
            for name, cls in inspect.getmembers(module)
                if inspect.isclass(cls)
    ]

def hex_to_rgb(value):
    value = value.lstrip('#')
    length = len(value)
    rvalue = tuple(int(value[i:i + length / 3], 16) for i in range(0, length, length / 3))
    return [rvalue[0] / 256, rvalue[1] / 256, rvalue[2] / 256]

def rgb_to_hex(r, g=None, b=None, a=None):
    if g == None or b == None:
        g = r[1] * 256
        b = r[2] * 256
        a = r[3] * 256
        r = r[0] * 256

    #return '#%02x%02x%02x' % (r, g, b)
    return '#%04x%04x%04x' % (r, g, b)
