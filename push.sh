#!/bin/bash
set -x
set -e
git clone https://${PERSONAL_TOKEN}@github.com/${GH_REPO}.git panda
cd panda
export BRANCH_NAME=devto-shop-random-generator
git --version
git config --global user.email "no-reply@gmail.com"
git config --global user.name "Devto Shop Random Generator"
git branch -d $BRANCH_NAME || true
git checkout -b $BRANCH_NAME
git add --all
git commit --message "create a random item from a budget" || exit 0
git remote add origin-$BRANCH_NAME https://${PERSONAL_TOKEN}@github.com/${GH_REPO}.git
git push --force --quiet --set-upstream origin-$BRANCH_NAME $BRANCH_NAME