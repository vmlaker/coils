"""Distutils file for coils module."""

from distutils.core import setup
from src import __version__

setup(
    name         = 'coils',
    version      = __version__,
    description  = 'Pure Python miscellanea.',
    url          = 'http://github.com/vmlaker/coils',
    author       = 'Velimir Mlaker',
    author_email = 'velimir.mlaker@gmail.com',
    license      = 'MIT',
    long_description = open('README.rst').read(),
    package_dir  = {'coils' : 'src'},
    packages     = ['coils'],
    )
