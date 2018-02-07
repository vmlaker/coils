.. _build_doc:

For developers
==============

Get the Coils source from GitHub:
::

   git clone https://github.com/vmlaker/coils
   cd coils

Run nosetests:
::

   nosetests `ls -d test/*.py` < test/user_input.txt

Create the build distribution:
::

   python setup.py bdist

Build the documentation:
::

   cd doc
   sh build-doc.sh
   cd ..

Update Python Package Index:
::

   python setup.py sdist upload -r https://pypi.python.org/pypi
