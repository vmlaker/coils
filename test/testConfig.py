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
    assert c['QUOTE'] == "Ehh, what's up doc?"
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
    assert c2['QUOTE'] == "Ehh, what's up doc?"
    c3 = Config()
    c3.load(fname2)
    assert c3['TOON'] == 'Bugs Bunny'
    assert c3['QUOTE'] == "Ehh, what's up doc?"
test4()

def test5():
    """Create empty config, and try to reload."""
    from Config import Config
    c = Config()
    assert c.reload() == False
test5()

def test6():
    """Create from file and test reload."""
    from os.path import join, dirname, abspath
    from Config import Config
    f = join(dirname(abspath(__file__)), 'simple.cfg')
    c = Config(f)
    c['QUOTE'] = "Gee, ain't I a stinker."
    assert c['QUOTE'] == "Gee, ain't I a stinker."
    assert c.reload() == True
    assert c['QUOTE'] == "Ehh, what's up doc?"
    c['ORIGIN'] = 'Warner Bros.'
    assert c['ORIGIN'] == 'Warner Bros.'
    assert c.reload() == True
    assert c['ORIGIN'] == None
test6()

def test7():
    """Create empty, and test load and reload."""
    from os.path import join, dirname, abspath
    from Config import Config
    c = Config()
    assert c.reload() == False
    f = join(dirname(abspath(__file__)), 'simple.cfg')
    c.load(f)
    c['QUOTE'] = "Gee, ain't I a stinker."
    assert c['QUOTE'] == "Gee, ain't I a stinker."
    assert c.reload() == True
    assert c['QUOTE'] == "Ehh, what's up doc?"
    c['ORIGIN'] = 'Warner Bros.'
    assert c['ORIGIN'] == 'Warner Bros.'
    assert c.reload() == True
    assert c['ORIGIN'] == None
test7()

def test8():
    """Test thread safety."""
    from os.path import join, dirname, abspath
    from threading import Thread
    from Config import Config
    f = join(dirname(abspath(__file__)), 'simple.cfg')
    c = Config(f)
    def threaded(config):
        for ii in range(100):
            config.reload()
            assert config['TOON'] == 'Bugs Bunny'
    threads = list()
    for ii in range(100):
        threads.append(Thread(target=threaded, args=(c,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
test8()
