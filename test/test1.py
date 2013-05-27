# -*- coding: utf-8 -*-
from coils import Config
c1 = Config()
c1['NAME'] = 'Bender'
c1['SURNAME'] = 'Rodríguez'
print(c1)

from os.path import join, dirname, abspath
fname = join(dirname(abspath(__file__)), 'test1.cfg')
c2 = Config(fname)
c2['FRUIT'] = 'apple'
print(c2['FRUIT'])
print(c2)
