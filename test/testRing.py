def test1():
    """Test the Ring data structure."""

    from Ring import Ring

    a = Ring([0,1,2])
    assert a[0] == 0
    assert a[1] == 1
    assert a[2] == 2
    assert a.first() == 0
    assert a.last() == 2

    a.turn()
    assert a[0] == 1
    assert a[1] == 2
    assert a[2] == 0
    assert a.first() == 1
    assert a.last() == 0

    a.turn()
    assert a[0] == 2
    assert a[1] == 0
    assert a[2] == 1
    assert a.first() == 2
    assert a.last() == 1
test1()
