#!/usr/bin/env python
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

import os, sys
from distutils.core import setup

def is_package(path):
    return (os.path.isdir(path) and os.path.isfile(os.path.join(path, '__init__.py')))

def find_packages(path, base=""):
    """ Find all packages in path """
    packages = {}
    for item in os.listdir(path):
        dir = os.path.join(path, item)
        if is_package(dir):
            if base:
                module_name = "%(base)s.%(item)s" % vars()
            else:
                module_name = item

            packages[module_name] = dir
            packages.update(find_packages(dir, module_name))

    return packages

packages = find_packages(".")
setup(
    name='agui',
    version='0.1',
    license='GPL-3',
    author='Brian Douglass',
    author_email='bhdouglass@gmail.com',
    description='One common interface for many different guis.',
    url='http://bhdouglass.tk/agui/',
    long_description='Use one api and dunamically use different guis, provided there is a ui file.',
    package_dir = packages,
    packages = packages.keys()
)
