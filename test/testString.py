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
