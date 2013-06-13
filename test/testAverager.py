def test1():
    """Test Averager."""
    from Averager import Averager
    a = Averager(0)  # Same as Averager(1)
    assert len(a) == 0
    assert a.add(1.0) == 1.0  # 1.0 / 1
    assert len(a) == 1
    assert a.add(2.0) == 2.0  # 2.0 / 1
    assert len(a) == 1
    assert a.add(3.0) == 3.0  # 3.0 / 1
test1()

def test2():
    """Test Averager."""
    from Averager import Averager
    a = Averager(2)
    assert len(a) == 0
    assert a.add(1.0) == 1.0  # 1.0 / 1
    assert len(a) == 1
    assert a.add(2.0) == 1.5  # (1.0 + 2.0) / 2
    assert len(a) == 2
    assert a.add(3.0) == 2.5  # (2.0 + 3.0) / 2
    assert len(a) == 2
test2()
