def test1():
    """Start from empty."""
    from coils import SortedList
    a = SortedList()
    for val in range(10):
        a.add(val)
    assert a.getCountLT(5) == 5
    assert a.getCountGT(5) == 4
    assert a.removeLT(5) == 5
    assert a.getCountLT(5) == 0

def test2():
    """Construct from list."""
    from coils import SortedList
    a = SortedList([b for b in range(10)])
    assert a.getCountLT(5) == 5
    assert a.getCountGT(5) == 4
    assert a.removeLT(5) == 5
    assert a.getCountLT(5) == 0
