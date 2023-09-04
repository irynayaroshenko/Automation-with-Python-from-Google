"""Amending Commits"""
# https://smartlogic.io/blog/git-commit-amend/

# If we made commit and realised that some files were not added or some file is not needed there, or our comment is not
# descriptive enough, we can edit (amend - make changes) that commit. When we run git commit --amend, git will take
# whatever is currently in our staging area and run the git commit workflow to overwrite the previous commit.
# git commit --amend allows us to modify and add changes to the most recent commit.

# git commit --amend


# git commit --amend -m "Updated message to amended commit"  (if we want to edit/change message)


# Say that your last commit is missing a crucial file. To change the files in a commit, first add the files you want to
# be included in your commit:

# git add redemption.exs


# If you want to remove a file from a commit, you can use git rm:

# git rm garbage.exs


# Once you have made the changes to a repository, you are ready to amend your commit. You can do this by using
# the –no-edit flag:

# git commit --amend --no-edit       (if we don't want to edit/change message)


# This command will change the files in your last commit. It will not change the message associated with the commit
# because we have not used the -m flag.


# NOTE!
# While git --amend is okay for fixing up local commits, you shouldn't use it on public commits.
# Meaning, those that have been pushed to a public or shared repository.
# This is because using --amend rewrites the git history removing the previous commit and replacing it with the amended
# one. This can lead to some confusing situations when working with other people and should definitely be avoided.
# So remember, fixing up a local commit with amend is great, and you can push it to a shared repository after you fixed
# it. But you should avoid amending commits that have already been made public.
