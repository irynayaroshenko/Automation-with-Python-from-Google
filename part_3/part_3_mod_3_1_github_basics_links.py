"""What is GitHub?"""

#  Git is a distributed version control system. Distributed means that each developer has a copy of the whole repository
# on their local machine. Each copy is a peer (analog) of the others. But we can host one of these copies on a server
# and then use it as a remote repository for the other copies. This lets us synchronize work between copies through
# this server.

# GitHub is a web-based Git repository hosting service. On top of the version control functionality of Git,
# GitHub includes extra features like bug tracking, wikis, and task management. It lets us share and access repositories
# on the web and copy or clone them to our local computer, so we can work on them.

"""Basic Interaction with GitHub"""
# open test_git_repo_on_github.png

# git clone <URL>


# Example:
# $ git clone https://github.com/irynayaroshenko/test_git.git
# Cloning into 'test_git'...
# remote: Enumerating objects: 3, done.
# remote: Counting objects: 100% (3/3), done.
# remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
# Receiving objects: 100% (3/3), done.

# push commits from your local repo to a remote repo:

# git push


# In order not to type our credentials each time, use command:

# git config --global credential.helper cache


# Now that we've enabled the credential helper, we'll need to enter our credentials once more.
# After that, they'll be cached for 15 minutes.

# retrieve new changes from the repository:

# git pull


"""Basic Interaction with GitHub Cheat-Sheet"""
# git clone URL
# used to clone a remote repository into a local workspace https://git-scm.com/docs/git-clone

# git push
# used to push commits from your local repo to a remote repo https://git-scm.com/docs/git-push

# git pull
# used to fetch the newest updates from a remote repository https://git-scm.com/docs/git-pull


# This can be useful for keeping your local workspace up to date:

# https://help.github.com/en/articles/caching-your-github-password-in-git

# https://help.github.com/en/articles/generating-an-ssh-key
