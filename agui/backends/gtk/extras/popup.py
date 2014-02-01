from agui.aextras import APopup
from agui.backends.gtk.imports import *

class Popup(APopup):
    def popup(self, title, message, icon):
        n = Notify.Notification.new(title, message, icon)
        n.show()
