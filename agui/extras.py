from agui import APP

if APP.is_gtk():
    from agui.backends.gtk.extras import *
elif APP.is_pyside():
    from agui.backends.pysdie.extras import *
else:
    raise RuntimeError('Backend gui not yet chosen')
