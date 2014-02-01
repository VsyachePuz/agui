class AttrDict(object):
    def __init__(self, **kwargs):
        self._dict = {}

        for key, value in kwargs.iteritems():
            self._dict[key] = value

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __getitem__(self, key):
        return self._dict[key]

    def __setattr__(self, key, value):
        if key != '_dict':
            self._dict[key] = value
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, key):
        if key != '_dict':
            return self._dict[key]
        else:
            return object.__getattr__(self, key)
