class App(object):
    version = '0.1'

    GTK = 'gtk'
    PYSIDE = 'pyside'

    GUIS = [GTK, PYSIDE]

    def __init__(self):
        self._tr = lambda s: s
        self._gui = ''

    @property
    def gui(self):
        return self._gui

    @gui.setter
    def gui(self, value):
        if self._gui != '':
            raise RuntimeError('Cannot change the gui backend once set')

        if value not in self.GUIS:
            raise ValueError('Choose an implemented gui backend')

        self._gui = value

        if self.gui == self.PYSIDE:
            from agui.backends.pyside.imports import QtGui
            self._app = QtGui.QApplication([""])

    def detect_gui(self):
        if self._gui == '':
            try:
                from agui.backends.gtk.imports import Gtk
                self.gui = self.GTK
            except:
                pass

        if self._gui == '':
            try:
                from agui.backends.pyside.imports import QtGui
                self.gui = self.PYSIDE
            except:
                pass

    def is_gtk(self):
        return (self.gui == self.GTK)

    def is_pyside(self):
        return (self.gui == self.PYSIDE)

    def run(self):
        if self.is_gtk():
            from agui.backends.gtk.imports import Gtk
            Gtk.main()
        elif self.is_pyside():
            self._app.exec_()

    def quit(self):
        if self.is_gtk():
            from agui.backends.gtk.imports import Gtk
            Gtk.main_quit()
        elif self.is_pyside():
            self._app.quit()

    @property
    def tr(self):
        return self._tr

    @tr.setter
    def tr(self, value):
        self._tr = value
