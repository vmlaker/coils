"""Defines Timer class."""

import datetime


class Timer:
    """Times duration of code blocks."""

    def __init__(self):
        """Initialize the object, marking the current time."""
        self._started = datetime.datetime.now()
        self._previous = self._started

    def getTotal(self):
        """Return a :class:`datetime.timedelta` object representing
        total time elapsed since construction."""
        now = datetime.datetime.now()
        result = now - self._started
        return result

    def get(self):
        """Return a :class:`datetime.timedelta` object representing
        time elapsed since object construction,
        or since last call to this function, whichever is more recent."""
        now = datetime.datetime.now()
        result = now - self._previous
        self._previous = now
        return result
