from agui import APP, Object, Signal

if APP.is_gtk():
    from agui.backends.gtk.widgets import *
elif APP.is_pyside():
    from agui.backends.pyside.widgets import *
else:
    raise RuntimeError('Backend gui not yet chosen')
