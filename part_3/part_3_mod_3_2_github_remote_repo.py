"""What is a remote?"""
# When working with remotes the workflow for making changes has some extra steps.
# We still modify stage and commit our local changes. After committing, we'll fetch any new changes from the remote repo
# manually merge if necessary (if any conflicts) and only then will push our changes to the remote repo.

# Git supports a variety of ways to connect to a remote repository.
# Some of the most common are using the HTTP, HTTPS and SSH protocols and their corresponding URLs.
# HTTP is generally used to allow read only access to a repository. In other words, it lets people clone the contents of
# your repo without letting them push new contents to it.
# Conversely, HTTPS and SSH, both provide methods of authenticating users, so we can control who gets permission to push

"""Working with Remotes"""
# go to dir with cloned repo, use commands below to get info about remote repo (open test_git_repo_on_github_1.png)

# git remote -v


# $ git remote -v
# origin  https://github.com/irynayaroshenko/test_git.git (fetch)
# origin  https://github.com/irynayaroshenko/test_git.git (push)

# Here we see the URLs associated with the origin remote. There are two URLs: one will be used to fetch data from the
# remote repository, and the other one to push data to that remote repo.
# They'll usually point at the same place.
# But in some cases, you can have the fetch URL use HTTP for read only access, and the push URL use HTTPS or SSH for
# access control.
# It's fine as long as the contents of the repo that you read when fetching are the same that you write to in pushing.
# Remote repositories have a name assigned to them, by default, the assigned name is 'origin'.
# This lets us track more than one remote in the same Git directory. While this is not the typical usage, it can be
# useful when collaborating with different teams on projects that are related to each other.


# more information about our remote:

# git remote show origin


# $ git remote show origin
# * remote origin
#   Fetch URL: https://github.com/irynayaroshenko/test_git.git
#   Push  URL: https://github.com/irynayaroshenko/test_git.git
#   HEAD branch: main
#   Remote branch:
#     main tracked
#   Local branch configured for 'git pull':
#     main merges with remote main
#   Local ref configured for 'git push':
#     main pushes to main (up to date)

# For now, we only have a main branch that exists locally and remotely. So the information here seems a bit repetitive.
# Once you start having more branches, especially different branches in the local and remote repo, this information
# starts becoming more complex.

# Whenever we're operating with remotes, Git uses remote branches to keep copies of the data that's stored in the remote
# repository.

# Get remote branches that Git repo is currently tracking:
#
# git branch -r


# $ git branch -r
#   origin/HEAD -> origin/main
#   origin/main

# These branches are read only.
# We can look at the commit history, like we would with local branches, but we can't make any changes to them directly.

# To modify their contents, we'll have to go through the workflow we called out before: pull any new changes to our
# local branch -> merge them with our changes -> push our changes to the repo.

# check the status of our changes in remote branches
#
# git status


# $ git status
# On branch main
# Your branch is up to date with 'origin/main'.

# Now that we're working with a remote repository, 'git status' gives us additional information.
# It tells us that our branch is up-to-date with the origin/main branch, which means that the main branch in the remote
# repository called origin, has the same commits as our local master branch.
