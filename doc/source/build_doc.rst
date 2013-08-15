.. _build_doc:

Building the docs
=================

The docs are generated using
`Sphinx documentation generator <http://sphinx-doc.org>`_. 

To begin, we first clone the repo *again* from the root directory.
I know, sounds weird, but that's how I configured Sphinx to work.
Sphinx uses that clone to parse docstrings from the source code
so that it can generate the pretty
`API page <api.html>`_.
You'll delete this directory after building the docs.
::

  git clone . coils

Now just run Make:
::

  make -C doc html

Go ahead and clean up the previously cloned repo:
::

  rm -rf coils







