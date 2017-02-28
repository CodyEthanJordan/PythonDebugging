#!/bin/bash

# Using git
# PHZ 3150 Introduction to Numerical Computing
# University of Central Florida Department of Physics
# 2017-02-27
# Cody Jordan

# set up a destination folder in your class directory
cd /mnt/c
mkdir GitLecture
cd GitLecture

# clone the repo that I made
git clone https://github.com/CodyEthanJordan/PythonDebugging

# this not only copies all the files, but also the whole repo and history
# git log will show the output of what has happened in the repo so far
# there are also GUI programs for this and a web interface
# https://github.com/CodyEthanJordan/PythonDebugging/commits/master
git log

# what did I do in commit 50bb64d95b2cfc208f6320eaaca9a1cab69785a0
git log 50bb64d95b2cfc208f6320eaaca9a1cab69785a0
# a commit is like a checkpoint, its a state of our code which we can return to
# Between each commit we make changes using git add, and git commit

# we can also specify only a part of the commit as long as it isn't ambiguous
git log 50bb

# what actual code changes did I make
cd GitExample
ls
git diff 50bb^ 50bb -- hw7_cjordan.py
# the ^ character means "the commit immediately prior to this"
# after the two dashes, --, we can give a specific filename which we are interested in

# git diff will show us what changed between two commits, in this case it reads as
# the commit before 50bb (thats what the ^ is), and commit 50bb itself, looking at
# the hw7_cjordan.py file
# Red text with minux signs is what got removed, text next to plus signs is added

# QUESTION: what did I change between 50bb and the next commit? and what message did I make?

# we can also reset the whole repo to this state and open the file
git checkout 50bb

# can open the files, look around
ls

# we can checkout the "master" branch again
git checkout master

# QUESTION: can you find a commit where the code won't run?

# A branch is a way to work on multiple things simultaneously, allowing you to
# make changes in parallel
# This is typically used when more than one person is working on the code, or
# to organize bugfixes and feature changes into logical units

# To show remote branches
git branch -r

# show all branches with a
git branch -a

# We can make a new branch with the git branch command
# after we make the new branch we can then checkout that branch to begin working
# in it
git branch FixingGarden
git checkout FixingGarden

# Now I can open my hw7_cjordan.py and make bugfixes

# Put in my changes
git status
git add GitExample/hw7_cjordan.py
git commit -m "Fixed rounding to whole numbers of plants"

# Merge my changes back in to the main branch
git checkout master
git merge FixingGarden

# Check to see what other changes we have?
git pull

# QUESTION: how do I incorporate this new branch from origin/

# now lets tag this as a release
git tag -a "Handin 7.0" -m "Tag releases to indicate this is what I am turning in"

# To push this branch to the remote I used
git push origin master --tags
# --tags indicate that I also want to upload all the tags which I made

# You can undo everything with reset
# git reset --hard
