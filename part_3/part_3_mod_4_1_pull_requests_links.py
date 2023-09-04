"""A Simple Pull Request on GitHub through the GitHub interface"""
# Forking is a way of creating a copy of the given repository so that it belongs to our user.
# In other words, our user will be able to push changes to the forked copy, even when we can't push changes to the
# other repo. When collaborating on projects hosted on GitHub, the typical workflows, first, create a fork of the repo,
# and then work on that local fork. A forked repo is just like a normal repo, except GitHub knows which repo it forked
# from. So we can eventually merge our changes back into the main repo by creating a pull request.
# A pull request is a commit or series of commits that you send to the owner of the repository so that they incorporate
# it into their tree. This is a typical way of working on GitHub, because in most projects, only a few people have
# commit rights to the repo. But anybody can suggest patches, bug fixes or even new features by sending pull requests
# that people with commit access can then apply.
# Typically, the owners of the repo will review the changes before merging them. Checking that they match the
# development guidelines for the project and that the license is valid and so on.

# Once we're done making changes to the file, we can make a change proposal, by scrolling down and filling in the
# description of the change. Clicking on the Proposed file change button, we'll create a commit in our forked repo,
# so that we can send the change to our colleague. To create pull request click 'Create pull request' button.

"""The Typical Pull Request Workflow on GitHub"""
# Create pull request directly on GitHub by using the web interface to edit files works for simple changes like fixing
# typos or adding documentation to a function, but it's not so great for making larger changes that we want to preview
# or test. For that, we'll normally have a local copy of the repo in computer and work with the forked repo as a remote.

# Go to needed repo on GitHub and create a fork by pressing the 'Fork' button. The copy will contain the current state
# of the repo including files and commit history. Once the fork is created, we're shown a page that corresponds
# to the same repo name, but it's under our user.

# Get a local copy of the repo (e.g., 'some_changes'):
# git clone <copied URL from button 'Clone or download'>

# cd some_changes
# ls -l
# git log     (to see commit history)

# Now that we have a local copy of the repo, we can make any changes we'd like to it. E.g., project doesn't have
# README.md file. To do that, we'll create a new branch called Add README.

# git checkout -b add-readme

# nano README.md   (create and put some text, save and exit: Crtl+O -> Enter -> Ctrl+X)

# git add README.md

# git commit -m "README.md was added for clear documentation"

# To push the change to our forked repo on GitHub (for the 1st time), we need to create the corresponding remote branch:

# git push -u origin add-readme

# When we push the change to the new branch, we got a message that we can create a pull request if we want to.
# If we look at the top of the Project page, GitHub tells us that our branch is ahead of the original repositories main
# branch by one commit, which is the commit we just made. We can start our pull requests by clicking 'Pull Request' link

# Before creating a pull request, it's always important to check that the code will merge successfully.
# GitHub tells us that our change can be automatically merged, which is great news. If this wasn't the case, we'd need
# to rebase our change against the current branch of the original repo so that it could be merged.

# Add useful comment in pull request (if it was tested, add info how: auto (add tests) or manually (how exactly)).

# It's always a good idea to double-check that we're sending the right change: look at the diff that appears at the
# bottom of the page.

# Finally, click 'Create pull request' button

"""Updating an Existing Pull Request"""
# When we send a pull request, it's pretty common to receive some comments from the project maintainers asking for some
# improvements.

# We make changes to needed file/files (nano <file_name>)

# git commit -am "Relevant comment for the commit"

# git push  (goes to GitHub)

# Then we can check our pull request on GitHub in 'Commits' tab. It's important to notice here that we just pushed our
# commit to the same branch as before and GitHub automatically added it to the pull request.
# If we wanted to create a separate pull request, we would need to create a new branch instead.

"""Squashing Changes"""
# You shouldn't rewrite history when the commits have been published. That's because someone else may have already
# synchronized that repo with those contents. This rule is waived with pull requests, since it's usually only you who
# have cloned your fork of the repository.

# Project maintainers may ask us to create a single commit that includes both changes and a more detailed description
# than the one we submitted.

# We can do that by using the interactive version of the 'rebase' called 'rebase -i', as the parameter to the command
# we pass 'main' branch.

# git rebase-i main

# When we call an interactive rebase, a text editor opens with a list of all the selected commits from the oldest to
# the most recent. (Open interactive_rebase_message.png)
# By changing the first word of each line, we can select what we want to do with the commits.

# The default action here is pick which takes the commits and re-bases them against the branch we selected.

# The comments in the file tells all the different commands we can use for our commits.
# For example, we can 'reword' a commit message keeping the changes as they are but modifying the commit message.
# We can also 'edit' the commit to add or remove changes from it.

# We have two options for combining commits: 'squash' and 'fixup'.
# In both cases, the contents of the selected commit are merged into the previous commit in the list.
# The difference is what happens with the commit messages.

# When we choose 'squash', the commit messages are added together and an editor opens up to let us make any necessary
# changes.
# When we choose 'fixup', the commit message for that commit is discarded.

# For our example, we want to use 'squash' so that we can combine both commits but also modify the commit description.
# So let's change the 'pick' command in the second line to 'squash' it into the first one, then we'll save and exit the
# editor as usual.

# Once we've told git that we want to squash a commit unto the one before it, we're given another file to edit.
# In this case, it's the combined commit message.
# As usual, git shows us some helpful information in the comments including which files are modified and what commits
# are being combined. We want to improve the description by adding more info about our change.

# Now that our commit contains the right information, we can save and exit as usual => rebase worked

# Let's check the latest commit and the changes in it:

# git show

# Our two changes have been combined into one that contains the whole new file and the right commit message.
# git status        - check info about current state

# Git tells us that our local branch has one commit, which is the rebase we just did.
# It also tells us that the origin/add-readme branch has two commits. These are the two commits we had already pushed
# to the repo.

# graph for the latest 4 commits

# git log --graph --one line --all -4

# We can see that the 2 commits pushed to the origin/add-readme branch show up in a different path than the commit
# that's currently in our local add-readme branch.
# This is expected whenever we do a rebase because the old commits are in the remote repo, and we have a different
# commit in our local repo.

# git push

# Push wasn't successful as git doesn't like us trying to push our change because it can't be fast-forwarded.
# But in this case, we don't want to create a merge. Instead, we want to replace the old commits with the new one.

# Force git to push the current snapshot into the repo as is

# git push -f

# This time, our push completed successfully.
# Git tells us here that we forced an update.

# Let's look once again our history graph:

# git log -- graph --one line --all -4

# This time, it's just one commit on top of master. The divergence is gone.

# Now let's look at the contents of the pull request. We've managed to combine both are commits into one by using the
# interactive version of 'git rebase'.


"""Git Fork and Pull Request Cheat Sheet"""

# https://help.github.com/en/articles/about-pull-request-merges
