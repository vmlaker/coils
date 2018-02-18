venv: requirements.txt
	virtualenv venv -p python3
	./venv/bin/pip install -r requirements.txt
	ln -sf ./venv/bin/python .

doc: venv
	rm -rf doc
	venv/bin/sphinx-quickstart doc < sphinx-qs-stdin.txt

	# So that it knows where Coils is installed.
	sed -i s:'# import os':'import os':g doc/source/conf.py
	sed -i s:'# import sys':'import sys':g doc/source/conf.py
	sed -i s:"# sys.path.insert(0, os.path.abspath('.'))":"sys.path.insert(0, os.path.abspath('../..'))":g doc/source/conf.py

	# Needed to have autodoc.
	sed -i s:"extensions = \[":"extensions = \['sphinx.ext.autodoc',":g doc/source/conf.py

	echo '\n# Add class and __init__ docstrings to the class doc.' >> doc/source/conf.py
	echo "autoclass_content = 'both'" >> doc/source/conf.py

	echo '\n# Do not prepend module name to all object names.' >> doc/source/conf.py
	echo "add_module_names = False" >> doc/source/conf.py

	cp logo.png doc/source/_static
	echo '\n# Add the logo.' >> doc/source/conf.py
	echo "html_logo = 'logo.png'" >> doc/source/conf.py

	# Generate the API docxs.
	cd doc && ../venv/bin/sphinx-apidoc --no-headings -o source ../coils/

	# So that make command below uses the right sphinx-build executable.
	sed -i s:'sphinx-build':`realpath venv/bin/sphinx-build`:g doc/Makefile

	cp index.rst doc/source

	cd doc && make html

clean:
	rm -rf doc python venv
