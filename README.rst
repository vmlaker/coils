.. image:: http://vmlaker.github.io/coils/logo.png
  :alt: Coils Logo

.. image:: https://api.travis-ci.org/vmlaker/coils.png?branch=master
  :alt: Build Result Image
  :target: https://travis-ci.org/vmlaker/coils

Coils
=====

My miscellaneous, standalone, 100% pure Python codes I use in other projects. 
It's not "officially packaged" in any way; just dump 
the directory in your own project's source tree 
and use it as a Python module:
::
  
  git clone http://github.com/vmlaker/coils

Or, consider cloning it as a Git submodule inside your own repo:
::

  git submodule add http://github.com/vmlaker/coils

By the way, the name "coils" is not tied to any of the codes inside.
You're free to call it whatever you want:
::

  git submodule add http://github.com/vmlaker/coils other/stuff/swirly
  touch other/__init__.py
  touch other/stuff/__init__.py
  python
  >>> from other.stuff import swirly
  >>> a = swirly.Averager(2)  # Average of last 2 values
  >>> a.add(1.0)
  1.0
  >>> a.add(2.0)
  1.5
  >>> a.add(3.0)
  2.5
