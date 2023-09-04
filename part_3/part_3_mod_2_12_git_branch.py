"""Creating New Branches"""
# open git_branch_1.png
# Note. Currently main branch is called 'main' by default, earlier it was called 'master' (like in video)

# Check all branches. Branch with * means you are on it, e.g. *main

# git branch


# create new branch and switch to it:

# git branch <new-branch-name>
# git checkout <new-branch-name>


# or with one command:

# git checkout -b <some-new-branch-name>

# create some file with some code, save, add and commit to branch. Check with 'git log -2'.
# We see the last two commits in this branch.
# Notice how next to the latest commit ID, git shows that this is where head is pointing to and that the branch is
# called even better feature (open git_branch_0.png). Next to the previous commit, git shows that both the master and
# the new feature branches are pointing to that snapshot of the project. In this way, we can see that the even better\
# feature branch is ahead of the master branch.

"""Working with Branches, Deleting"""
# When we switch branches in git, the working directory and commit history will be changed to reflect the snapshot
# of our project in that branch. When we check out a new branch and commit on it, those changes will be added to
# the history of that branch.
# Shortly, if we created, modified and committed files on <some-new-branch-name> and then switched to main via
# 'git checkout main', all those files won't be present on main (till we explicitly merge them).

# switch to main:

# git checkout main


# to delete a branch you must not be on it. Switch e.g. to main then delete other branch (if no unmerged files there):

# git branch -d <branch-name>


# Output:
# Deleted branch first_new_branch (was 4592ff8).

# If there are unmerged files on branch, git shows warning:

# $ git branch -d second_new_branch
# error: The branch 'second_new_branch' is not fully merged.
# If you are sure you want to delete it, run 'git branch -D second_new_branch'

# If you don't plan to merge those files, use:

# git branch -D <branch-name>


"""Merging"""

# !! Fast-forward merge !!

# merge your branch with main (note: all files on your branch should be committed). Shortly: you switch to branch
# where you want to add changes from your branch:

# git checkout main
# git merge <your-branch-name>

# After this 'git log' will show that HEAD points at main. We can see test_branch_for_merge and main branches are now
# both pointing at the same commit. (Merging combines branched data and history together.)

# commit 2df939dafd86bb8d90d5f68e7bb7a1261a95fd43 (HEAD -> main, test_branch_for_merge)
# Author: ira_yar <irina.yaroshenko99@gmail.com>
# Date:   Fri Jul 7 16:34:00 2023 +0300
#
#     test file committed


# Git uses 2 different algorithms to perform a merge: fast-forward and three-way merge.

# Fast-forward merge occurs when all the commits in the checked out branch are also in the branch that's being merged.
# If this is the case, we can say that the commit history of both branches doesn't diverge.
# In these cases, all Git has to do is update the pointers of the branches to
# the same commit, and no actual merging needs to take place.

# On the other hand, a three-way merge is performed when the history of the merging branches has diverged in some way,
# and there isn't a nice linear path to combine them via fast-forwarding.
# This happens when a commit is made on one branch after the point when both branches split.

# When this occurs, Git will tie the branch histories together with a new commit.
# And merge the snapshots at the two branch tips with the most recent common ancestor, the commit before the divergence.

# To do this successfully, Git tries to figure out how to combine both snapshots.
# If the changes were made in different files, or in different parts of the same
# file, Git will take both changes and put them together in the result.
# If instead the changes are made on the same part of the same file, Git won't
# know how to merge those changes, and the attempt will result in a merge conflict.









