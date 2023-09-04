"""Skipping the Staging Area"""
# If we want to commit several files without staging (without 'git add'), use flag -a or -am (the same as '-a -m'). But
# it should be previously staged file, not new. If the modified file has never been committed to the repo,
# we'll still need to use 'git add' to track it first.

# git commit -am "Commit modified file all_changes.py without staging"

# When you use the -a shortcut, you skip the staging area.
# Meaning, you can't add any other changes before creating the commit. So you need to be sure that you've already
# included everything you want to include in that commit. In the end, using a shortcut like '-a' is just like using
# the regular commit workflow. The commit will show up in the log along with the message just as usual.

# i_yaroshenko@DM-NB-108 MINGW64 ~/checks (main)
# $ git log
# commit 2ce41b541e84d3da6848cae63a81890e9d55bd9d (HEAD -> main)
# Author: ira_yar <irina.yaroshenko99@gmail.com>
# Date:   Thu Jul 6 20:51:02 2023 +0300
#
#     Commit without staging modified file all_checks.py

# Git uses the HEAD alias to represent the currently checked out snapshot of your project.
# This lets you know what the contents of your working directory should be.
# In this case, the current snapshot is the latest commit in the project.

# In all cases, HEAD is used to indicate what the currently checked out snapshot is.
# This is how git marks your place in the project.

# When you run git commands like 'diff', 'branch', or 'status', git will use the HEAD bookmark as
# a basis for whatever operation it's performing.

# As a shortcut, it's generally easy to think of HEAD as a pointer to the current branch, although it can be more
# powerful than that.








