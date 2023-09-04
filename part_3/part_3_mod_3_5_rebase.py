"""Rebasing Your Changes  (merging feature branches back into the main trunk of our code)"""

# Once our branch has been properly reviewed and tested, it can get merged back into the master branch.
# This can be done by us or by someone else. One option is to use 'git merge'.
# Another option - use 'git rebase'. Rebasing means changing the base commit that's used for our branch. Moves the current branch on top of our remote branch.

# We run the command 'git rebase', followed by the branch that we want to set as the new base.
# When we do this, Git will try to replay our commits after the latest commit in that branch.
# This will work automatically if the changes are made in different parts of the files, but will require manual
# intervention if the changes were made in other files.

# Let's check out this process by rebasing our refactor branch onto the master branch.
# First, we'll check out the master branch and pull the latest changes in the remote repo.

# open rebase_example.png
# Here the refactor branch has three commits before the common ancestor, with the current commit that's at the head
# of the master branch. If we merged our branch now, it would cause a three-way merge. But we want to keep our history
# linear. We'll do this with a rebase of the refactor against master.

# Rebase local changes before pushing to clean up your work, but never rebase anything that you’ve pushed somewhere.

# !! Watch and read !! : https://www.themoderncoder.com/a-better-git-workflow-with-rebase/
# Read: https://www.atlassian.com/git/tutorials/merging-vs-rebasing

# git checkout main
# git pull
# git log --graph --oneline --all
# git checkout refactor (branch from video. open three_way_merge.png)
# git rebase main
# git log --graph --oneline
# git checkout main
# git merge refactor
# git push --delete origin refactor    (remove the remote branch)
# git push -d refactor                 (remove the local branch)
# git push

"""Another Rebasing Example. fetch-rebase-push  (making sure that our commits made in the master branch apply cleanly on
top of the current state of the master branch)"""

# One common example is to rebase the changes in the master branch when someone else also made changes, and we want to
# keep history linear.
# This is a pretty common occurrence when you're working on a change that's small enough not to need a separate branch
# and your collaborators just happened to commit something at the same time.

# nano all_checks.py  * explanation to code
# git commit -am "Add a simple network connectivity check"
# git fetch
# git rebase origin/main
# * conflict occurred in health_checks.py (open conflict_during_rebase.png). We resolve it.
# ./health_checks.py  (test it works after resolving conflict)
# git add health_checks.py
# git rebase --continue     - rebase finishes successfully
# git log --graph --oneline   - check how graph now looks like (open conflict_during_rebase_solve_push.png)
# git push

"""Best Practices for Collaboration"""

# 1. Always synchronize your branches before starting any work on your own.
# 2. Try and avoid having very large changes that modify a lot of different things. Instead, try to make changes as
# small as possible as long as they're self-contained.
# 3. When working on a big change, it makes sense to have a separate feature branch.
# 4. Regularly merge changes made on the master branch back onto the feature branch.
# 5. If you need to maintain more than one version of a project at the same time, it's common practice to have the
# latest version of the project in the master branch and a stable version of the project on a separate branch. You'll
# merge your changes into the separate branch whenever you declare a stable release.
# 6. You shouldn't rebase changes that have been pushed to remote repos. (Git server will automatically reject pushes
# that attempt to rewrite the history of the branch. It's possible to force Git to accept the change, but
# it's not a great idea unless you really know what the implications will be.)
# 7. Having good commit messages is important.

# Whenever we collaborate with others, there's bound to be some merge conflicts, and they can sure be a pain.
# I've definitely been frustrated when encountering complex merge conflicts and trying to debug the results.
# If I'm dealing with this type of merge conflict, my first step is to work backward and disable everything I've done
# and then see if the source still works, then I slowly add pieces of code until I hit the problem.

# TODO Complete code to health_checks.py from screenshots

# * explanation to code
# Now that we've made it easy to add new checks, will add a check to warn when there's no working network.
# There's a ton of things to check for this but for now we'll keep it simple and just check whether we can resolve
# google.com URL.
# To do this, we'll use the socket module. We'll add a new function called 'check_no_network' that will return
# True if it fails to resolve the URL and False if it succeeds.
# This socket.gethostbyname function raises an exception on failure.
# So we'll use it try except block to wrap the call to the function and return False when the call succeeds or True when
# it fails.
# With this new function defined, we can now add the check to our list of checks.
# We'll just add the name of the function and the message will be, "No working network."

