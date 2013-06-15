def test1():
    """Test string2time() function."""

    from String import string2time

    text = '2013-06-15 14:09:11.456789'
    assert '{0}'.format(string2time(text)) == '{0}'.format(text)

    text = '2013-06-15 14:09:11.45678'
    assert '{0}'.format(string2time(text)) == '{0}0'.format(text)

    text = '2013-06-15 14:09:11.456'
    assert '{0}'.format(string2time(text)) == '{0}000'.format(text)

    text = '2013-06-15 14:09:11.4'
    assert '{0}'.format(string2time(text)) == '{0}00000'.format(text)

    text = '2013-06-15 14:09:11'
    assert '{0}'.format(string2time(text)) == '{0}'.format(text)

test1()

def test2():
    """Test time2string() function."""
    from datetime import datetime
    from String import time2string
    a = datetime.now()
    assert '{0}'.format(a) == '{0}'.format(time2string(a))
test2()

def test3():
    """Test time2levels() function."""
    from datetime import datetime
    from String import time2levels, string2time
    t1 = datetime.now()
    assert len(time2levels(t1)) == 5
    t2 = string2time('2013-06-15 16:30:18')
    assert time2levels(t2) == ['2013', '06', '15', '16', '30']
test3()

def test4():
    """Test time2dir() function."""
    from os.path import join
    from datetime import datetime
    from String import time2dir, string2time
    t1 = string2time('2013-06-15 16:30:18')
    assert time2dir(t1) == join('2013', '06', '15', '16', '30')
test4()

def test5():
    """Test time2fname() function."""
    from os.path import join
    from datetime import datetime
    from String import time2fname, string2time
    t1 = string2time('2013-06-15 16:30:18')
    assert time2fname(t1) == '__2013-06-15__16:30:18:000000__'
    assert time2fname(t1, full=True) == '\
2013/06/15/16/30/__2013-06-15__16:30:18:000000__'
test5()
