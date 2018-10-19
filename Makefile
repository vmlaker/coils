.PHONY: docs

venv: requirements.txt
	virtualenv venv -p python3
	./venv/bin/pip install -r requirements.txt
	ln -sf ./venv/bin/python .

test: venv
	./python setup.py install
	./python setup.py test

coverage: test
	./venv/bin/coverage run coils/test/test*.py
	./venv/bin/coverage report

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
	  --no-batchfile \
	  --no-makefile

	cp logo.png docs/_static/
	echo '\n# Add the logo.' >> docs/conf.py
	echo "html_logo = 'logo.png'" >> docs/conf.py

	echo '\n# Add class and __init__ docstrings to the class doc.' >> docs/conf.py
	echo "autoclass_content = 'both'" >> docs/conf.py

	sed -i s:"exclude_patterns = \[":"exclude_patterns = \['modules.rst', ":g docs/conf.py

	cp about.rst coils.rst index.rst docs
	sed -i s:"@VERSION@":$(VERSION):g docs/*.rst
	sed -i s*"@DATE@"*"$(DATE)"*g docs/*.rst

	./venv/bin/sphinx-apidoc -o docs coils
	./venv/bin/sphinx-build -b html docs/ docs/_build/html/

init-gh-pages: docs
	rm -rf html docs/_build/html
	ln -sf ../../html docs/_build/html
	git clone git@github.com:vmlaker/coils.git html
	cd html && \
	git branch gh-pages && \
	git checkout gh-pages && \
	git symbolic-ref HEAD refs/heads/gh-pages && \
	rm .git/index && \
	git clean -fdx
	git ci -m 'First pages commit.'
	git push origin gh-pages

MASTER_VERSION = $(shell git log master -1 | head -1)

gh-pages: docs
	rm -rf html
	#git clone https://github.com/vmlaker/coils.git html
	git clone git@github.com:vmlaker/coils.git html
	cd html && git checkout gh-pages
	rm -rf html/*
	cp -r docs/_build/html/* html
	cd html && touch .nojekyll
	cd html && git add .
	cd html && git commit -m 'Update gh-pages for $(MASTER_VERSION).'
	cd html && git push origin gh-pages

clean:
	rm -rf build dist docs html python venv
	rm -rf .coverage .eggs coils.egg-info index.tex
	find . -name '*.pyc' -exec rm {} \;
