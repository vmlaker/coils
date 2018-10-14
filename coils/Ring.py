"""Defines the Ring class.

The code, before slight variation in turn() method, was taken from:
  http://code.activestate.com/recipes/52246-implementing-a-circular-data-structure-using-lists
"""


class Ring:
    """Circular data structure implemented as a list."""

    def __init__(self, donor):
        """Initialize the ring with a donor list."""
        if not donor:
            raise 'Ring must have at least one element.'
        self._data = donor

    def __repr__(self):
        return repr(self._data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def turn(self):
        """Turn the ring for a single position.
        For example, [a, b, c, d] becomes [b, c, d, a]."""
        first = self._data.pop(0)
        self._data.append(first)

    def first(self):
        """Return the first entry."""
        return self._data[0]

    def last(self):
        """Return the last entry."""
        return self._data[-1]
