"""Useful string conversions and such."""

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
