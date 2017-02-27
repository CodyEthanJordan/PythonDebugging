#!/bin/bash

# Using git
# PHZ 3150 Introduction to Numerical Computing
# University of Central Florida Department of Physics
# 2017-02-27
# Cody Jordan

# set up a destination folder in your class directory
cd ~
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

# we can also specify only a part of the commit as long as it isn't ambiguous
git log 50bb

# what actual code changes did I make
cd GitExample
ls
git diff 50bb^ 50bb -- hw7_cjordan.py

# git diff will show us what changed between two commits, in this case it reads as
# the commit before 50bb (thats what the ^ is), and commit 50bb itself, looking at
# the hw7_cjordan.py file
# Red text with minux signs is what got removed, text next to plus signs is added

# we can also reset the whole repo to this state
git checkout 50bb

# can open the files, look around
# to go back we can check out the main branch again
git checkout master

# QUESTION: what did I change between 50bb and the next commit? and what message did I make?




# In order to make this example I first made a new branch
git commit -b NewBranch

# To push this branch to the remote I used
git push origin master


# To show remote branches
git branch -r

# Local branches with
git branch -a

# To blow everyting up
git reset --hard
git checkout master

# To go to a previous commit
git checkout CommitIDTHingy

# Can also check out tags
git checkout Part1
