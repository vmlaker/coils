"""Defines SortedList class."""

import bisect


class SortedList(object):
    """Maintains a list of sorted items, with fast trimming
    using less-than/greater-than comparison."""

    def __init__(self, donor=list()):
        """Initialize the object with a copy of the donor list, sorted."""
        self._list = sorted(donor[:])

    def add(self, item):
        """Add item to the list while maintaining sorted order."""
        bisect.insort_left(self._list, item)

    def getCountLT(self, item):
        """Return number of elements less than *item*."""
        index = bisect.bisect_left(self._list, item)
        return index

    def getCountGT(self, item):
        """Return number of elements greater than *item*."""
        index = bisect.bisect_right(self._list, item)
        return len(self._list) - index

    def removeLT(self, item):
        """Trim off any elements less than *item*.
        Return number of elements trimmed."""
        count = self.getCountLT(item)
        self._list = self._list[count:]
        return count
