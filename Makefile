.PHONY: docs

venv: requirements.txt
	virtualenv venv -p python3
	./venv/bin/pip install -r requirements.txt
	ln -sf ./venv/bin/python .

test: venv
	./venv/bin/nose2 < coils/test/user_input.txt

VERSION = `./python -c 'import coils; print(coils.__version__)'`
DATE = `date +"%B %e, %Y"`

docs: venv
	rm -rf docs
	venv/bin/sphinx-quickstart docs < sphinx-qs-stdin.txt

	# So that it knows where Coils is installed.
	sed -i s:'# import os':'import os':g docs/source/conf.py
	sed -i s:'# import sys':'import sys':g docs/source/conf.py
	sed -i s:"# sys.path.insert(0, os.path.abspath('.'))":"sys.path.insert(0, os.path.abspath('../..'))":g docs/source/conf.py

	# Needed to have autodoc.
	sed -i s:"extensions = \[":"extensions = \['sphinx.ext.autodoc',":g docs/source/conf.py

	echo '\n# Add class and __init__ docstrings to the class doc.' >> docs/source/conf.py
	echo "autoclass_content = 'both'" >> docs/source/conf.py

	echo '\n# Show the toctree in sidebar of each page.' >> docs/source/conf.py
	echo "html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'], }" >> docs/source/conf.py

	cp logo.png docs/source/_static
	echo '\n# Add the logo.' >> docs/source/conf.py
	echo "html_logo = 'logo.png'" >> docs/source/conf.py

	# Generate the API docxs.
	cd docs && ../venv/bin/sphinx-apidoc --no-headings -o source ../coils/

	# So that make command below uses the right sphinx-build executable.
	sed -i s:'sphinx-build':`realpath venv/bin/sphinx-build`:g docs/Makefile

	cp *.rst docs/source
	sed -i s:"@VERSION@":$(VERSION):g docs/source/*.rst
	sed -i s*"@DATE@"*"$(DATE)"*g docs/source/*.rst
	cd docs && make html

clean:
	rm -rf build docs python venv
	find . -name '*.pyc' -exec rm {} \;
