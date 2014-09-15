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

from agui.aextras import APopup

use_pynotify = False
use_notify2 = False
try:
    import pynotify
    pynotify.init('remindor')
    use_pynotify = True
except:
    import notify2
    notify2.init('remindor')
    use_notify2 = True

class Popup(APopup):
    def popup(self, app, title, message, icon):
        if use_pynotify:
            n = pynotify.Notification(title, message, icon)
            n.show()
        elif use_notify2:
            n = notify2.Notification(title, message, icon)
            n.show()

        #TODO: fallback to use tray icon messages
        #TODO: init pynotify
