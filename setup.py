from distutils.core import setup
from src import __version__

setup(
    name         = 'coils',
    version      = __version__,
    description  = 'A small library of generic codes written in 100% pure Python.',
    url          = 'http://vmlaker.github.io/coils',
    author       = 'Velimir Mlaker',
    author_email = 'velimir.mlaker@gmail.com',
    license      = 'MIT',
    #long_description = open('README.rst').read(),
    package_dir  = {'coils' : 'src'},
    packages     = ['coils'],
    classifiers  = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Freeware',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
