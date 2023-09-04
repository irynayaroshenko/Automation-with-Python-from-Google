"""Merge Conflicts"""
# To reproduce conflict (open merge_conflict_1.png):
# - edit the same line/-s of code in the same file on different branches
# - add and commit each such file on each branch
# - switch to main
# - merge other branch to main

# Result:
# $ git merge test_branch_for_merge
# Auto-merging test_file.py
# CONFLICT (content): Merge conflict in test_file.py
# Automatic merge failed; fix conflicts and then commit the result.
#
# i_yaroshenko@DM-NB-108 MINGW64 ~/checks (main|MERGING)
# $ git status
# On branch main
# You have unmerged paths.
#   (fix conflicts and run "git commit")
#   (use "git merge --abort" to abort the merge)
#
# Unmerged paths:
#   (use "git add <file>..." to mark resolution)
#         both modified:   test_file.py
#
# no changes added to commit (use "git add" and/or "git commit -a")

# Next step: being on main, open conflicted file (open merge_conflict_2.png):
# import sys
#
# def hello():
# <<<<<<< HEAD
#   return 'Hello, world! And comment from main for merge conflict'
# =======
#   return 'Hello, world! Now some words from test_branch'
# >>>>>>> test_branch_for_merge
#   sys.exit(0)

# You can leave both options (not in this case because we can't have 2 return statements as is) or one of it and delete
# merge markers. In our case solving conflict looks:
# import sys
#
# def hello():
#   return 'Hello, world! Now some words from test_branch'
#   sys.exit(0)


# add file to stage: git add <file_name>
# commit: git commit - opens window for message with message about merge (open merge_conflict_3.png). This description
# was automatically created when we called the git merge command.

# Result after committing: [main e63bec3] Merge branch 'test_branch_for_merge' (means everything ok).


# !! Observe log graph !!   open merge_conflict_4.png

# git log --graph --oneline

# $ git log --graph --oneline
# *   e63bec3 (HEAD -> main) Merge branch 'test_branch_for_merge'
# |\
# | * d41df04 (test_branch_for_merge) Change on test branch for merge conflict
# * | 9e868de Added change on main for merge conflict
# |/
# * 2df939d test file committed
# * 4592ff8 Revert "Remaning file"
# * 4f1bde0 Revert "Test file added"
# * 86d7c5b Test file added
# * 573ada7 Revert "Commit output.txt file and test command without -m" My comment added
# * 5075414 Commit output.txt file and test command without -m
# * 5708455 Some updated message
# * 0987e60 Added .DS_STORE to .gitignore
# * 03d98f1 Remaning file
# * 7aff8f5 Delete unneeded file 'capitalize_words.py'
# * 0206d24 Added message 'Everything ok'
# * 2ce41b5 Commit without staging modified file all_checks.py
# * bc217de Commit all files from stage area to git directory.
# * da5edf1 First file added to test git repo


# # git log --graph     (shows more lines for each commit)


# git merge --abort

# Merge conflicts can sometimes be tricky, complicated, and spread across multiple files.
# If you want to throw the merge away and start over, you can use the 'git merge --abort' command as an escape hatch.
# This will stop the merge and reset the files in your working tree back to the previous commit before the merge ever
# happened.


"""Git Branches and Merging Cheat Sheet"""

# Command     Explanation & Link

# git branch
# Used to manage branches https://git-scm.com/docs/git-branch

# git branch <name>
# Creates the branch https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

# git branch -d <name>
# Deletes the branch https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--D

# git branch -D <name>
# Forcibly deletes the branch https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--D

# git checkout <branch>
# Switches to a branch https://git-scm.com/docs/git-checkout

# git checkout -b <branch>
# Creates a new branch and switches to it https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt--bltnewbranchgt

# git merge <branch>
# Merge joins branches together https://git-scm.com/docs/git-merge

# git merge --abort
# If there are merge conflicts (meaning files are incompatible), --abort can be used to abort the merge action.

# git log --graph --oneline
# This shows a summarized view of the commit history for a repo https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History
