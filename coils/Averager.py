"""Defines Averager class."""

import collections


class Averager(object):
    """Keeps a running average with limited history."""

    def __init__(self, max_count):
        """Initialize the averager with maximum number of
        (latest) samples to keep."""
        self._max_count = max_count if max_count > 1 else 1  # Minimum is 1.
        self._data = collections.deque()

    def add(self, value):
        """Add a value, and return current average."""
        self._data.append(value)
        if len(self._data) > self._max_count:
            self._data.popleft()
        return sum(self._data)/len(self._data)

    def __len__(self):
        """Length operator."""
        return len(self._data)
