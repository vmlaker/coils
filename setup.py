"""Distutils file for coils module."""

from distutils.core import setup

setup(
    name         = 'coils',
    version      = '0.0.1',
    description  = 'Pure Python miscellanea.',
    url          = 'http://github.com/vmlaker/coils',
    author       = 'Velimir Mlaker',
    author_email = 'velimir.mlaker@gmail.com',
    license      = 'MIT',
    long_description = open('README.rst').read(),
    package_dir  = {'coils' : 'src'},
    packages     = ['coils'],
    )
