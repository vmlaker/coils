from setuptools import setup

exec(open('./coils/version.py').read())

setup(
    name='coils',
    version=__version__,
    description='A tiny library of generic codes written in 100% pure Python.',
    url='http://vmlaker.github.io/coils',
    author='Velimir Mlaker',
    author_email='velimir.mlaker@gmail.com',
    license='MIT',
    packages=['coils'],
    setup_requires=[
        'pytest-runner==4.2',
    ],
    tests_require=[
        'pydocstyle==2.1.1',
        'pytest-cov==2.6.0',
        'pytest-pep8==1.0.6',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Freeware',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
