# Shell script to build gh-pages.
# Run from root directory.

# Switch to gh-pages branch and start afresh.
git checkout gh-pages

# Remove everything execept the logo.
# TODO: Change gh-pages to use logo in master branch (raw)
#       so we don't have to pick-n-choose here.
rm -rf *.html *.js objects.inv _static _sources

# Switch to master branch (Sphinx build needs doc/.)
git checkout master setup.py src doc
git reset HEAD

# Build the docs and move html/ files to root directory.
python setup.py bdist
cd doc
sh build-doc.sh
cd ..
mv -fv doc/build/html/* .

# Remove the directories (from master branch) needed for building docs.
rm -rf setup.py src build dist doc

# Add everything to gh-pages.
git add --all

# Commit with comment referencing latest master branch commit.
git commit -m "Updated gh-pages for `git log master -1 | head -1`"

# Push.
#git push origin gh-pages
