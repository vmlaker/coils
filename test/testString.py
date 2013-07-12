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

def test11():
    """Test string2time() function with partial strings."""

    from String import string2time
    for (arg, out) in (
        ('', 'None'),
        ('2', 'None'),
        ('20', 'None'),
        ('201', 'None'),
        ('2013', '2013-01-01 00:00:00'),
        ('2013-', '2013-01-01 00:00:00'),
        ('2013-0', 'None'),
        ('2013-07', '2013-07-01 00:00:00'),
        ('2013-07-', '2013-07-01 00:00:00'),
        ('2013-07-1', '2013-07-01 00:00:00'),
        ('2013-07-12', '2013-07-12 00:00:00'),
        ('2013-07-12 ', '2013-07-12 00:00:00'),
        ('2013-07-12 0', '2013-07-12 00:00:00'),
        ('2013-07-12 08', '2013-07-12 08:00:00'),
        ('2013-07-12 08:', '2013-07-12 08:00:00'),
        ('2013-07-12 08:2', '2013-07-12 08:02:00'),
        ('2013-07-12 08:26', '2013-07-12 08:26:00'),
        ('2013-07-12 08:26:', '2013-07-12 08:26:00'),
        ('2013-07-12 08:26:2', '2013-07-12 08:26:02'),
        ('2013-07-12 08:26:22', '2013-07-12 08:26:22'),
        ('2013-07-12 08:26:22.', '2013-07-12 08:26:22'),
        ('2013-07-12 08:26:22.4', '2013-07-12 08:26:22.400000'),
        ('2013-07-12 08:26:22.45', '2013-07-12 08:26:22.450000'),
        ('2013-07-12 08:26:22.456', '2013-07-12 08:26:22.456000'),
        ('2013-07-12 08:26:22.4567', '2013-07-12 08:26:22.456700'),
        ('2013-07-12 08:26:22.45678', '2013-07-12 08:26:22.456780'),
        ('2013-07-12 08:26:22.456789', '2013-07-12 08:26:22.456789'),
        ):
        assert str(string2time(arg)) == out
test11()

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
