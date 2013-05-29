"""Defines Averager class."""

import collections

class Averager(object):
    """Keeps a running average with limited history."""

    def __init__(self, size):
        """Initialize the object with maximum size of sampled data."""
        self._size = size
        self._data = collections.deque()

    def add(self, value):
        """Add a value, and return current average."""
        self._data.append(value)
        if len(self._data) > self._size:
            self._data.popleft()
        return sum(self._data)/len(self._data)
