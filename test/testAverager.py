def test1():
    """Test Averager."""
    from coils import Averager
    a = Averager(2)
    assert a.add(1.0) == 1.0  # 1.0 / 1
    assert a.add(2.0) == 1.5  # (1.0 + 2.0) / 2
    assert a.add(3.0) == 2.5  # (2.0 + 3.0) / 2
