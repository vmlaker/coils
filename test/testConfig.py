# -*- coding: utf-8 -*-

def test1():
    """Start from empty, set and get."""
    from Config import Config
    c = Config()
    c['NAME'] = 'Bender'
    c['SURNAME'] = 'Rodríguez'
    assert c['NAME'] == 'Bender'
    assert c['SURNAME'] == 'Rodríguez'
test1()

def test2():
    """Read from file and get."""
    from os.path import join, dirname, abspath
    from Config import Config
    fname = join(dirname(abspath(__file__)), 'simple.cfg')
    c = Config(fname)
    assert c['TOON'] == 'Bugs Bunny'
    assert c['QUOTE'] == 'The quick brown fox jumped over the lazy dog.'
test2()

def test3():
    """Read from file containing erroneous line, and get."""
    from os.path import join, dirname, abspath
    from Config import Config
    fname = join(dirname(abspath(__file__)), 'simple2.cfg')
    c = Config(fname)
    assert c['Kingdom'] == 'Animalia'
    assert c['Genus'] == 'Python'
test3()

def test4():
    """Read from file, get, save, load via constructor and load()."""
    from os.path import join, dirname, abspath
    from Config import Config
    fname1 = join(dirname(abspath(__file__)), 'simple.cfg')
    c1 = Config(fname1)
    fname2 = join(dirname(abspath(__file__)), 'test4.out')
    c1.save(fname2)
    c2 = Config(fname2)
    assert c2['TOON'] == 'Bugs Bunny'
    assert c2['QUOTE'] == 'The quick brown fox jumped over the lazy dog.'
    c3 = Config()
    c3.load(fname2)
    assert c3['TOON'] == 'Bugs Bunny'
    assert c3['QUOTE'] == 'The quick brown fox jumped over the lazy dog.'
test4()
