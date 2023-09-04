"""The Pull-Merge-Push Workflow"""

# if we push our changes to remote repo and Git rejected our change, that's because the remote repository contains
# changes that we don't have in our local branch that Git can't fast-forward. We need to pull changes from remote repo:

# git pull

# If we get conflicts (Output has: Automatic merge failed; fix conflicts and check commit result), we can see the graph
# which shows the different commits and positions in the tree:

# git log --graph --oneline --all

# open three_way_merge.png. This graph shows us the different commits and positions in the tree.
# We can see the master branch, the origin/master branch, and the experimental branch.
# The graph indicates that our current commit and the commit in the origin/master branch share a common ancestor,
# but they don't follow one another.

# Here we need to do a three-way merge. To do this, let's look at the actual changes:

# git log -p origin/main

# 1. Then we solve the conflicts by editing files and choosing needed lines
# 2. git add <edited files with resolved conflicts>
# 3. git commit (without -m) - window for comment opens. We can add extra message there.
# 4. git push

# When Git needs to do a three-way merge, we end up with a separate commit for merging the branches back into the main tree.


"""Pushing Remote Branches"""
# If we need make new feature or refactor code or fix bug, etc., create separate remote branch:

# git checkout -b <branch_name>

# make all work on the branch, git add, git commit and when ready push to remote repo (not to main yet), do:

# git push -u origin <branch_name>    ** Explanation


# Result (open push_remote_branch.png):
# $ git push -u origin refactor
# Enumerating objects: 4, done.
# Counting objects: 100% (4/4), done.
# Delta compression using up to 16 threads
# Compressing objects: 100% (2/2), done.
# Writing objects: 100% (3/3), 318 bytes | 318.00 KiB/s, done.
# Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
# remote:
# remote: Create a pull request for 'refactor' on GitHub by visiting:
# remote:      https://github.com/irynayaroshenko/test_git/pull/new/refactor
# remote:
# To https://github.com/irynayaroshenko/test_git.git
#  * [new branch]      refactor -> refactor

# ** Explanation:
# Before we merge any of this into the master branch, we want to push this into the remote repo, so that our
# collaborators can view the code, test it, and let us know if it's ready for merging.
# The first time we push a branch to a remote repo, we need to add a few more parameters to the Git push command.
# We'll need to add the '-u' flag to create the branch upstream, which is another way of referring to remote repositories.
# We'll also have to say that we want to push this to the 'origin' repo, and that we're pushing the <branch_name> branch.
