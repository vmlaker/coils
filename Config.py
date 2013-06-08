"""A simple loadable, saveable, one-line-per-entry config."""

class Config(object):
    
    def __init__(self, fname=None):
        """Create config object, optionally load from file."""
        self._fname = fname
        self._data = dict()
        if fname:
            self.load(fname)

    def load(self, fname=None):
        """Load config with contents of file."""
        if fname:
            self._load_from_file(fname)
        elif self._fname:
            self._load_from_file(self._fname)

    def save(self, fname=None):
        """Save config to file."""
        if fname:
            self._save_to_file(fname)
        elif self._fname:
            self._save_to_file(self._fname)

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
            result += '%s %s'%(key, self._data[key])
        return result
    
    def _load_from_file(self, fname):
        """Low-level load implementation."""
        with open(fname, 'r') as f:
            count = -1
            for line in f.readlines():
                count += 1
                line = line.strip()
                if not line:
                    continue
                if line[0] == '#':
                    continue
                if len(line) < 2:
                    print('Error line %d file %s'%(count, fname))
                    continue
                key = line.split()[0]
                val = line[len(key):].lstrip()
                self._data[key] = val

    def _save_to_file(self, fname):
        """Low-level save implementation."""
        f = open(fname, 'w')
        f.write(str(self))
        f.close()
