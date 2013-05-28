# -*- coding: utf-8 -*-

def test1():
    """Start from empty, set and get."""
    from coils import Config
    c = Config()
    c['NAME'] = 'Bender'
    c['SURNAME'] = 'Rodríguez'
    assert c['NAME'] == 'Bender'
    assert c['SURNAME'] == 'Rodríguez'

def test2():
    """Read from file and get."""
    from os.path import join, dirname, abspath
    from coils import Config
    fname = join(dirname(abspath(__file__)), 'simple.cfg')
    c = Config(fname)
    assert c['TOON'] == 'Bugs Bunny'
    assert c['QUOTE'] == 'The quick brown fox jumped over the lazy dog.'
