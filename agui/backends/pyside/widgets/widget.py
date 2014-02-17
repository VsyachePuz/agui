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
from agui.awidgets import AWidget

class Widget(AWidget):
    button_left = QtCore.Qt.LeftButton
    button_middle = QtCore.Qt.MiddleButton
    button_right = QtCore.Qt.RightButton

    def __init__(self, item = None):
        #AWidget.__init__(self, item)

        def mousePressEvent(widget, event):
            self.button_press.emit(event.button(), event.x(), event.y())
            event.accept()

        def mouseReleaseEvent(widget, event):
            self.button_release.emit(event.button(), event.x(), event.y())
            event.accept()

        def mouseDoubleClickEvent(widget, event):
            self.double_button_press.emit(event.button(), event.x(), event.y())
            event.accept()

        self.item.mousePressEvent = mousePressEvent
        self.item.mouseReleaseEvent = mouseReleaseEvent
        self.item.mouseDoubleClickEvent = mouseDoubleClickEvent

    @AWidget.hidden.getter
    def hidden(self):
        self._hidden = self.item.isHidden()
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        if value:
            self.item.hide()
        else:
            self.item.show()

        self._hidden = value

    @AWidget.enabled.getter
    def enabled(self):
        self._enabled = self.item.isEnabled()
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value:
            self.item.enable()
        else:
            self.item.disable()

        self._enabled = value

    @AWidget.context_menu.setter
    def context_menu(self, value):
        self._context_menu = value

        current_actions = self.item.actions()
        for action in current_actions:
            self.item.removeAction(action)

        actions = self._context_menu.actions()
        for action in actions:
            self.item.addAction(action)
