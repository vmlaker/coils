class Config(object):
    
    def __init__(self, fname=None):
        self.fname = fname
        self.data = {}
        if fname:
            self.load(fname)

    def load(self, fname=None):
        if fname:
            self._load_from_file(fname)
        elif self.fname:
            self._load_from_file(self.fname)
        pass

    def save(self, fname=None):
        if fname:
            self._save_to_file(fname)
        elif self.fname:
            self._save_to_file(self.fname)

    def __setitem__(self, key, val):
        self.data[key] = val
        
    def __getitem__(self, key):
        if key not in self.data:
            return None
        return self.data[key]

    def __str__(self):
        result = ''
        for key in sorted(self.data.keys()):
            if result:
                result += '\n'
            result += '%s %s'%(key, self.data[key])
        return result
    
    def _load_from_file(self, fname):
        f = open(fname, 'r')
        count = -1
        for line in f.readlines():
            count += 1
            line = line.strip()
            if not len(line):
                continue
            if line[0] == '#':
                continue
            if len(line) < 2:
                print('Error line %d file %s'%(count, fname))
                continue
            key = line.split()[0]
            val = line[len(key):].lstrip()
            self.data[key] = val
        f.close()

    def _save_to_file(self, fname):
        f = open(fname, 'w')
        f.write(str(self))
        f.close()

# The end.
