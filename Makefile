venv: requirements.txt
	virtualenv venv -p python3
	./venv/bin/pip install -r requirements.txt
	ln -sf ./venv/bin/python .

doc: venv
	rm -rf doc
	venv/bin/sphinx-quickstart doc < sphinx-qs-input.txt

	# So that it knows where Coils is installed.
	cd doc && sed -i s:'# import os':'import os':g source/conf.py
	cd doc && sed -i s:'# import sys':'import sys':g source/conf.py
	cd doc && sed -i s:"# sys.path.insert(0, os.path.abspath('.'))":"sys.path.insert(0, os.path.abspath('../..'))":g source/conf.py

	# Needed to have autodoc.
	cd doc && sed -i s:"extensions = \[":"extensions = \['sphinx.ext.autodoc',":g source/conf.py

	# So that the class and __init__ doc are added as class docstrings.
	cd doc && echo "autoclass_content = 'both'" >> source/conf.py

	# So that module name *is not* prepended to all object names.
	cd doc && echo "add_module_names = False" >> source/conf.py

	# Generate the API docxs.
	cd doc && ../venv/bin/sphinx-apidoc -o source ../coils/

	# So that make command below uses the right sphinx-build executable.
	cd doc && sed -i s:'sphinx-build':`realpath ../venv/bin/sphinx-build`:g Makefile

	cd doc && make html

clean:
	rm -rf doc python venv
