def test1():
    """Tick a simple ticker."""
    from RateTicker import RateTicker
    a = RateTicker((1,))
    assert a.tick() == (1.0,)
test1()

def test2():
    """Tick a three-period ticker."""
    from RateTicker import RateTicker
    a = RateTicker((1,2,5,))
    assert a.tick() == (1.0, 0.5, 0.2)
test2()
