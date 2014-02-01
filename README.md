# AGui #

Use one api and dunamically use different guis, provided there is a ui file.

## Dependencies ##

AGui requires the following dependencies:

Gtk Backend (Ubuntu & Family):

`sudo apt-get install gir1.2-notify-0.7 gir1.2-gtk-3.0 gir1.2-glib-2.0 gir1.2-gstreamer-0.10 gir1.2-appindicator3-0.1`

PySide Backend (Ubuntu & Family):

`sudo apt-get install python-pyside.qtcore python-pyside.qtgui python-pyside.qtuitools python-pyside.phonon python-pyside.qtsvg python-notify`

## Install ##

From source: `sudo python setup.py install`

## Testing ##

AGui uses nose for testing, simply run the command `nosetests --where=tests` from the root of this repository.

To install nose on Ubuntu & Family:
`sudo apt-get install python-nose`

## License ##

Copyright (C) 2014 Brian Douglass

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License version 3, as published 
by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranties of MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
