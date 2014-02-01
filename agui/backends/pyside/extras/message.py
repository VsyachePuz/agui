from agui.backends.pyside.imports import *
from agui.aextras import AMessage

class Message(AMessage):
    def message(self, window_title, title, message, icon):
        message2 = "<b>%s</b><br/><br/>%s" % (title, message)
        self.message(window_title, message2, icon)

    def message(self, window_title, message, icon):
        self.dialog = QtGui.QMessageBox(icon.icon(), window_title, message, QtGui.QMessageBox.Close)
        self.dialog.show()
