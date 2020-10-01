#!/bin/bash
set -x
set -e
python3 $4/main.py $1 $4
git clone https://$2@github.com/$3.git panda
ls
cp DEVTOSHOP.md panda
cd panda
export BRANCH_NAME=devto-shop-random-generator
git --version
git config --global user.email "rinoakbr@gmail.com"
git config --global user.name "spiritbro1"
git branch -d $BRANCH_NAME || true
git checkout -b $BRANCH_NAME
git add --all
git commit --message "create a random item from a budget" || exit 0
git remote add origin-$BRANCH_NAME https://$2@github.com/$3.git
git push --force --quiet --set-upstream origin-$BRANCH_NAME $BRANCH_NAME
