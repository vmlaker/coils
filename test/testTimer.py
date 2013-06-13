def test1():
    """Test Timer class."""
    from time import sleep
    from datetime import timedelta
    from Timer import Timer
    timer = Timer()
    sleep(0.001)
    assert timer.get() > timedelta(seconds=0.001)
    sleep(0.001)
    assert timer.get() > timedelta(seconds=0.001)
    assert timer.getTotal() > timedelta(seconds=0.002)
test1()
