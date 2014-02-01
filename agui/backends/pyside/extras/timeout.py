from agui.backends.pyside.imports import *
from agui.aextras import ATimeout

class Timeout(ATimeout):
    def start(self):
        ATimeout.start()
        self.item = QtCore.QTimer.singleShot(1000 * self.seconds, self.function)

    def stop(self):
        ATimeout.stop()
        self.item.stop()
