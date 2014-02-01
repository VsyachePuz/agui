from agui.aextra import APopup
import pynotify

class Popup(APopup):
    def popup(self, title, message, icon):
        n = pynotify.Notification(title, message, icon)
        n.show()
        #TODO: fallback to use tray icon messages
        #TODO: init pynotify
