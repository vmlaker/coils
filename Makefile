venv: requirements.txt
	virtualenv venv -p python3
	./venv/bin/pip install -r requirements.txt
	ln -sf ./venv/bin/python .

test: venv
	./venv/bin/nose2 < coils/test/user_input.txt

VERSION = `./python -c 'import coils; print(coils.__version__)'`
DATE = `date +"%B %e, %Y"`

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

	echo '\n# Show the toctree in sidebar of each page.' >> doc/source/conf.py
	echo "html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'], }" >> doc/source/conf.py

	cp logo.png doc/source/_static
	echo '\n# Add the logo.' >> doc/source/conf.py
	echo "html_logo = 'logo.png'" >> doc/source/conf.py

	# Generate the API docxs.
	cd doc && ../venv/bin/sphinx-apidoc --no-headings -o source ../coils/

	# So that make command below uses the right sphinx-build executable.
	sed -i s:'sphinx-build':`realpath venv/bin/sphinx-build`:g doc/Makefile

	cp *.rst doc/source
	sed -i s:"@VERSION@":$(VERSION):g doc/source/*.rst
	sed -i s*"@DATE@"*"$(DATE)"*g doc/source/*.rst
	cd doc && make html

clean:
	rm -rf doc python venv
