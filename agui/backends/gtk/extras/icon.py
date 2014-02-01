from agui.aextras import AIcon
from agui.backends.gtk.imports import *

class Icon(AIcon):
    def __init__(self, name, fallback = ''):
        self._use_fallback = not Gtk.IconTheme.has_icon(self.name)

    def icon(self, size = None):
        self.item = Gtk.Image()

        if self._use_fallback:
            size2 = Gtk.IconSize.BUTTON
            if size == self.size_menu:
                size2 = Gtk.IconSize.MENU
            elif size == self.size_dialog:
                size2 = Gtk.IconSize.DIALOG

            self.item.set_from_icon_name(self.name, size2)
        else:
            self.item.set_from_file(self.fallback)

        return self.item
