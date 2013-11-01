#!/bin/bash
python poachr2.py $1
git diff --exit-code
if [ "$?" -ne "0" ]; then
  git add names.txt
  git add nsids.txt
  git commit -m "Updating $1" --date=$1
fi