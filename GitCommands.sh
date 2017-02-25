#!/bin/bash

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

