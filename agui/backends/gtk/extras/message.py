from agui.aextras import AMessage
from agui.backends.gtk.imports import *

class Message(AMessage):
    def message(self, window_title, title, message, icon):
        dialog = Gtk.MessageDialog(flags=Gtk.DialogFlags.MODAL, message_format=title)
        dialog.set_image(icon.icon(icon.size_dialog))
        dialog.set_title(window_title)
        dialog.format_secondary_text(message)
        dialog.show()

    def message(self, window_title, message, icon):
        dialog = Gtk.MessageDialog(flags=Gtk.DialogFlags.MODAL, message_format=message)
        dialog.set_image(icon.icon(icon.size_dialog))
        dialog.set_title(window_title)
        dialog.show()
