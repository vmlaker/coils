.PHONY: docs

venv: requirements.txt
	virtualenv venv -p python3
	./venv/bin/pip install -r requirements.txt
	ln -sf ./venv/bin/python .

test: venv
	./python setup.py install
	./python setup.py test

dist: clean venv
	./python setup.py sdist bdist_wheel

testpypi: dist
	./venv/bin/twine upload --repository testpypi dist/*

pypi: dist
	./venv/bin/twine upload dist/*

VERSION = `./python -c 'import coils; print(coils.__version__)'`
DATE = `date +"%B %e, %Y"`
TIMESTAMP = $(shell date +%Y-%m-%d_%H:%M:%S)

docs: venv
	rm -rf docs
	./python setup.py install
	./venv/bin/sphinx-quickstart docs \
	  --quiet \
	  --project='Coils' \
	  --author='Velimir Mlaker' \
	  -v `./python -c 'import coils; print(coils.__version__)'` \
	  --dot=_ \
	  --ext-autodoc \
	  --ext-viewcode \
	  --no-batchfile \
	  --no-makefile

	cp logo.png docs/_static/
	echo '\n# Add the logo.' >> docs/conf.py
	echo "html_logo = 'logo.png'" >> docs/conf.py

	echo '\n# Add class and __init__ docstrings to the class doc.' >> docs/conf.py
	echo "autoclass_content = 'both'" >> docs/conf.py

	cp *.rst docs
	sed -i s:"@VERSION@":$(VERSION):g docs/*.rst
	sed -i s*"@DATE@"*"$(DATE)"*g docs/*.rst
	./venv/bin/sphinx-apidoc -o docs coils
	./venv/bin/sphinx-build -b html docs/ docs/_build/html/

clean:
	rm -rf build dist docs python venv
	rm -rf .coverage .eggs coils.egg-info
	find . -name '*.pyc' -exec rm {} \;
