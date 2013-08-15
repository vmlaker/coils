Original docs template created with Sphinx 1.1.3
by running the following commands from project root directory:
::

  sphinx-quickstart
  sed -i s:"#sys.path.insert(0, os.path.abspath('.'))":"sys.path.insert(0, os.path.abspath('../..'))":g doc/source/conf.py
  sphinx-apidoc -o doc/source/ .
