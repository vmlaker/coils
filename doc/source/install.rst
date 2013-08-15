.. _install:

How to install
==============

Just clone the repo somewhere, 
even inside your own project's source tree if you want:
::

  git clone http://github.com/vmlaker/coils

Run nosetests:
::

  nosetests `ls -d coils/test/*.py` < coils/test/user_input.txt

Write some code using the Coils module:
::

  python
  >>> from coils import Averager
  >>> a = Averager(2)  # Average of last 2 values
  >>> a.add(1.0)
  1.0
  >>> a.add(2.0)
  1.5
  >>> a.add(3.0)
  2.5
