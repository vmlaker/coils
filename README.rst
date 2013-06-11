coils
=====

.. image:: https://api.travis-ci.org/vmlaker/coils.png
  :alt: Build Result Image
  :target: https://travis-ci.org/vmlaker/coils

Some of my miscellaneous, 100% pure Python codes.

coils is written so you can use it as a Python module 
in your own project's source tree. Simply clone
the repo wherever you see fit:
::
  
  git clone http://github.com/vmlaker/coils

Or, if you're inside your own Git repo, you might 
prefer to clone coils as a Git submodule instead:
::

  git submodule add http://github.com/vmlaker/coils

Now you're ready to rock:
::

  python
  >>> import coils
  >>> r = coils.RateTicker((1, 5, 15))
  >>> r.tick()
  (1.0, 0.2, 0.06666666666666667)

If you can't (or just don't want to) use the name "coils",
you're free to call it whatever you want, no problem:
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
