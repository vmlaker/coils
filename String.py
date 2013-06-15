"""Useful string conversions and such."""

from os.path import join
from datetime import datetime

MICRO = '.%f'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S' + MICRO

def string2time(text):
    """Return datetime object from given string.
    Attempt to translate the string with microseconds, and if that
    fails, translate it without microseconds."""
    try:
        return datetime.strptime(text, TIME_FORMAT)
    except:
        return datetime.strptime(text, TIME_FORMAT[:-len(MICRO)])

def time2string(tstamp, micro=True):
    """Return time string, given a datetime object."""
    tformat = TIME_FORMAT if micro else TIME_FORMAT[:-len(MICRO)]
    return tstamp.strftime(tformat)

def time2levels(tstamp):
    """Return a list of directory levels (as strings) given a datetime object.
         E.g. given 2011-09-25 13:01:44,
              return ['2011', '09', '25', '13', '01'] 
    """
    return [tstamp.strftime(xx) for xx in ('%Y', '%m', '%d', '%H', '%M')]

def time2dir(tstamp):
    """Return assembly of os.path.join()s for given tstamp."""
    result = ''
    for field in time2levels(tstamp):
        result = join(result, field)
    return result

FILENAME_FORMAT = '__%Y-%m-%d__%H:%M:%S:%f__'

def time2fname(tstamp, full=False):
    result = tstamp.strftime(FILENAME_FORMAT)
    result = result if not full else join(time2dir(tstamp), result)
    return result
