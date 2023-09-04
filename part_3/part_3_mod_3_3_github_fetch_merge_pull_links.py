"""Fetching New Changes"""
# If command 'git remote show origin' or 'git status' shows that 'local out of date', we can sync data:

# git fetch


# it copies the commits done in the remote repo to the remote branches, so we can see what other people have committed.

# use command to observe commits/changes on main:

# git log origin/main


# use command to observe what can be pulled:

# git status


# we can merge the changes of main branch of the remote repository into our local branch (it's fast-forward merge):

# git merge origin/main


# 'git log' now shows the new commit, and that now our master branch is up-to-date with the remote origin/master branch.


# Instead of using 'git fetch' + 'git merge' we can use 'git pull'

# We can use 'git fetch' like this to review the changes that happen in the remote repository.
# If we're happy with them, we can use 'git merge' to integrate them into the local branch.

# If we don't want to review changes but just get changes to local repo, we use 'git pull'


# check what files were pulled after 'git pull':

# git log -p    or   git log -p -1

# If new branch appeared in remote repo (which was created by our colleague) we can 'git checkout <other branch>' and
# immediately local copy of that branch appears in our local repo.

# This way we got the contents of the <other branch> together with those of the master branch when we called 'git pull',
# which also merged new changes onto the master branch.
# If we want to get the contents of remote branches !without! automatically merging any contents into the local
# branches, we can call 'git remote update'.
# This will fetch the contents of all remote branches, so that we can just call checkout or merge as needed.

"""Git Remotes Cheat-Sheet"""

# git remote
# Lists remote repos https://git-scm.com/docs/git-remote

# git remote -v
# List remote repos verbosely https://git-scm.com/docs/git-remote#Documentation/git-remote.txt--v

# git remote show <name>
# Describes a single remote repo https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emshowem

# git remote update
# Fetches the most up-to-date objects https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emupdateem

# git fetch
# Downloads specific objects https://git-scm.com/docs/git-fetch

# git branch -r
# Lists remote branches can be combined with other branch arguments to manage remote branches
# https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--r
