venv: requirements.txt
	virtualenv venv -p python3
	./venv/bin/pip install -r requirements.txt
	ln -sf ./venv/bin/python .

doc: venv
	rm -rf doc
	mkdir doc
	cd doc && ../venv/bin/sphinx-quickstart < ../sphinx-qs-input.txt
	cd doc && sed -i s:'# import os':'import os':g source/conf.py
	cd doc && sed -i s:'# import sys':'import sys':g source/conf.py
	cd doc && sed -i s:"# sys.path.insert(0, os.path.abspath('.'))":"sys.path.insert(0, os.path.abspath('../..'))":g source/conf.py
	cd doc && sed -i s:"extensions = \[":"extensions = \['sphinx.ext.autodoc',":g source/conf.py
	cd doc && echo "autoclass_content = 'both'" >> source/conf.py
	cd doc && ../venv/bin/sphinx-apidoc -o source ../coils/
	cd doc && make html

clean:
	rm -rf doc python venv
