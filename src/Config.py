"""A micro config utility,
loadable, saveable, one-line-per-entry config class."""

import copy
import threading

class Config(object):

    def _deco(func):
        """Decorator that protects function with a lock."""
        def wrap(self, *args, **kwargs):
            with self._rlock:
                return func(self, *args, **kwargs)
        return wrap

    def __init__(self, fname=None):
        """Create config object, optionally load from file."""
        self._fname = fname
        self._data = dict()
        self._rlock = threading.RLock()
        if self._fname:
            self.load(self._fname)

    @_deco
    def load(self, fname):
        """Load config with contents of file."""
        self._fname = fname
        with open(self._fname, 'r') as f:
            count = -1
            for line in f.readlines():
                count += 1
                line = line.strip()
                if not line:
                    continue
                if line[0] == '#':
                    continue
                key = line.split()[0]
                val = line[len(key):].lstrip()
                if not val:
                    print('Error line {0} file {1}'.format(count, self._fname))
                    continue
                self._data[key] = val

    @_deco
    def reload(self):
        """Clear and reload the dictionary.
        Return True if successful, False otherwise."""
        if self._fname is None:
            return False
        data_copy = self._data.copy()
        self._data.clear()
        try:
            self.load(self._fname)
        except:
            self._data = data_copy
            return False
        return True

    @_deco
    def save(self, fname):
        """Save config to file."""
        with open(fname, 'w') as f:
            f.write(str(self))

    @_deco
    def items(self):
        """Return a copy of (key, value) pairs."""
        return self._data.items()

    @_deco
    def __setitem__(self, key, val):
        """Add entry using index operator."""
        self._data[key] = val
        
    @_deco
    def __getitem__(self, key):
        """Retrieve entry using index operator."""
        if key not in self._data:
            return None
        return self._data[key]

    @_deco
    def __str__(self):
        """Return string representation."""
        result = ''
        for key in sorted(self._data):
            if result:
                result += '\n'
            result += '{0} {1}'.format(key, self._data[key])
        return result
