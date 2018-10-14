"""Useful string conversions and such."""

from os.path import join
from datetime import datetime

MICRO = '.%f'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S' + MICRO


def string2time(text):
    """Return :class:`datetime.datetime` object from given string,
    or ``None`` if failed to translate."""
    length = len(TIME_FORMAT)
    result = None
    while length:
        try:
            result = datetime.strptime(text, TIME_FORMAT[:length])
        except:
            length -= 1
        else:
            break
    return result


def time2string(tstamp, micro=True):
    """Given a :class:`datetime.datetime` object,
    return a formatted time string."""
    tformat = TIME_FORMAT if micro else TIME_FORMAT[:-len(MICRO)]
    return tstamp.strftime(tformat)


def time2levels(tstamp):
    """Given a :class:`datetime.datetime` object,
    return a list of directory levels (as strings).

    For example, given "2013-09-08 13:01:44",
    return ['2013', '09', '08', '13', '01']
    """
    return [tstamp.strftime(xx) for xx in ('%Y', '%m', '%d', '%H', '%M')]


def time2dir(tstamp):
    """Given a :class:`datetime.datetime` object,
    return a path assembled with :func:`os.path.join`
    for the levels."""
    result = ''
    for field in time2levels(tstamp):
        result = join(result, field)
    return result

FILENAME_FORMAT = '__%Y-%m-%d__%H:%M:%S:%f__'


def time2fname(tstamp, full=False):
    """Return full path to filename prefix (i.e. without dot extension)
    represented by given :class:`datetime.datetime` object."""
    result = tstamp.strftime(FILENAME_FORMAT)
    result = result if not full else join(time2dir(tstamp), result)
    return result
