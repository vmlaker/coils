.. _build_doc:

Building the docs
=================

The docs are generated using
`Sphinx documentation generator <http://sphinx-doc.org>`_. 

To begin, copy all ``*.py`` files to a subdirectory called "coils".
Sphinx uses this *pseudo-package* to parse docstrings 
from the source code so that it can generate the pretty
`API page <api.html>`_.
You'll delete this directory after building the docs.
::

   mkdir coils
   cp *.py coils

Now just run Make using the makefile in ``doc/``:
::

   make -C doc html

Go ahead and browse the docs to make sure they look good.
When you're done, clean up the previously created directory:
::

   rm -rf coils
