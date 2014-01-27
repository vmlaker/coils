"""A micro config utility,
loadable, saveable, one-line-per-entry config class."""

class Config(object):
    
    def __init__(self, fname=None):
        """Create config object, optionally load from file."""
        self._data = dict()
        if fname:
            self.load(fname)

    def load(self, fname):
        """Load config with contents of file."""
        with open(fname, 'r') as f:
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
                    print('Error line {0} file {1}'.format(count, fname))
                    continue
                self._data[key] = val

    def save(self, fname):
        """Save config to file."""
        with open(fname, 'w') as f:
            f.write(str(self))

    def items(self):
        """Return a copy of (key, value) pairs."""
        return self._data.items()

    def __setitem__(self, key, val):
        """Add entry using index operator."""
        self._data[key] = val
        
    def __getitem__(self, key):
        """Retrieve entry using index operator."""
        if key not in self._data:
            return None
        return self._data[key]

    def __str__(self):
        """Return string representation."""
        result = ''
        for key in sorted(self._data):
            if result:
                result += '\n'
            result += '{0} {1}'.format(key, self._data[key])
        return result
