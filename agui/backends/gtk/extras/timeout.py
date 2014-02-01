from agui.aextras import ATimeout
from agui.backends.gtk.imports import *

class Timeout(ATimeout):
    def start(self):
        ATimeout.start()
        self.item = GObject.timeout_add(1000 * self.seconds, self.function)

    def stop(self):
        ATimeout.stop()
        GObject.source_remove(self.item)
