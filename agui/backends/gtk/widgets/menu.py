from agui.backends.gtk.imports import *
from agui.awidgets import AMenu
from agui.backends.gtk.widgets import Widget

class Menu(Widget, AMenu):
    def __init__(self):
        AMenu.__init__(self)

    def _create_item(self):
        self.item = Gtk.Menu()

    def append(self, text, icon = None):
        menu_item = None
        if icon is None:
            menu_item = Gtk.ImageMenuItem()
            menu_item.set_use_stock(False)
            menu_item.set_image(self.icon.icon())
        else:
            menu_item = Gtk.MenuItem()

        menu_item.set_label(text)
        menu_item.connect('activate', self.emit_triggered)
        menu_item.show()
        self.item.append(menu_item)

    def get_text(self, widget):
        return widget.get_label()

    def popup(self, widget, event):
        self.item.popup(None, None, None, None, event.button, event.time)
