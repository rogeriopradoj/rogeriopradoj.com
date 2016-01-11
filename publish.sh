#!/usr/bin/env sh
# make the script fail for any failed command
set -e
# make the script display the commands it runs to help debugging failures
set -x

# Go to the output directory
cd output_prod

# Remove the existing repo if it exists
if [ -d ".git" ]; then
    rm -rf .git
fi

# Create a repo for the built website for the master branch
git init

# configure env (locally)
git config user.email 'rogeriopradoj@gmail.com'
git config user.name 'RogerioPradoJ.com bot'

# commit build
git add .
git commit -m "Build website"

# push to GitHub Pages
git push "https://github.com/rogeriopradoj/rogeriopradoj.github.io" -f master
