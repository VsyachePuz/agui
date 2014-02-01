import inspect

def find_classes(module):
    return [
        cls
            for name, cls in inspect.getmembers(module)
                if inspect.isclass(cls)
    ]

def hex_to_rgb(value):
    value = value.lstrip('#')
    length = len(value)
    rvalue = tuple(int(value[i:i + length / 3], 16) for i in range(0, length, length / 3))
    return [rvalue[0] / 256, rvalue[1] / 256, rvalue[2] / 256]

def rgb_to_hex(r, g=None, b=None, a=None):
    if g == None or b == None:
        g = r[1] * 256
        b = r[2] * 256
        a = r[3] * 256
        r = r[0] * 256

    #return '#%02x%02x%02x' % (r, g, b)
    return '#%04x%04x%04x' % (r, g, b)
