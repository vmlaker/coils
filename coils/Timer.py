"""Defines Timer class."""

from datetime import datetime


class Timer:
    """Can be used like a timer or a stopwatch to measure time duration
    between clicks."""

    def __init__(self):
        """Initialize the object, marking the current time."""
        self._started = self._previous = datetime.now()

    def getTotal(self):
        """Return the number of seconds elapsed since object creation."""
        return (datetime.now() - self._started).total_seconds()

    def get(self):
        """Return the number of seconds elapsed since object creation,
        or since last call to this function, whichever is more recent."""
        elapsed = datetime.now() - self._previous
        self._previous += elapsed
        return elapsed.total_seconds()
