# Shell script to build gh-pages.
# Run from root directory.

# Switch to gh-pages branch and start afresh.
git checkout gh-pages
#rm -rf *

# Switch to master branch (Sphinx build needs doc/.)
git checkout master doc
git reset HEAD

# Clone the repo.
git clone http://github.com/vmlaker/coils

# Build the docs and move html/ files to root directory.
make -C doc html
mv -fv doc/build/html/* .

# Remove the directories (from master branch) needed for building docs.
rm -rf doc coils

# Add everything to gh-pages.
git add .

# Commit with comment referencing latest master branch commit.
git commit -m "Updated gh-pages for `git log master -1 | head -1`"

# Push.
#git push origin gh-pages
