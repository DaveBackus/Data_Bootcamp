#! /bin/bash
git pull origin master
hugo
ghp-import -n -p public
