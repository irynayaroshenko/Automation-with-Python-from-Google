"""Tracking Files"""
# When we operate with Git, our files can be either tracked or untracked.
# Tracked files are part of the snapshots, while untracked files aren't a part of snapshots yet.
# This is the usual case for new files. Each track file can be in one of three main states:
# modified, staged or committed.

# modified:
# it means that we've made changes to file that we haven't committed yet.
# The changes could be adding, modifying or deleting the contents of the file.
# Git notices anytime we modify our files.
# But won't store any changes until we add them to the staging area.

# staged:
# git addd - to stage those changes.
# When we do this, our modified files become stage files.
# In other words, the changes to those files are ready to be committed to the project.
# All files that are staged will be part of the next snapshot we take.

# committed:
# git commit - commit file
# When a file gets committed, the changes made to it are safely stored in a snapshot in the Git directory.

# Example of commands and outputs:
# $ git status
# On branch main
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         new file:   capitalize_words.py
#         new file:   rearrange.py
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
#         modified:   disc_usage_fixed.py
#
#
# i_yaroshenko@DM-NB-108 MINGW64 ~/checks (main)
# $ git add disc_usage_fixed.py
#
# i_yaroshenko@DM-NB-108 MINGW64 ~/checks (main)
# $ git status
# On branch main
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         new file:   capitalize_words.py
#         modified:   disc_usage_fixed.py
#         new file:   rearrange.py
#
#
# i_yaroshenko@DM-NB-108 MINGW64 ~/checks (main)
# $ git commit - m 'Commit all files from stage area to git directory.'
# error: pathspec '-' did not match any file(s) known to git
# error: pathspec 'm' did not match any file(s) known to git
# error: pathspec 'Commit all files from stage area to git directory.' did not match any file(s) known to git
#
# i_yaroshenko@DM-NB-108 MINGW64 ~/checks (main)
# $ git commit -m 'Commit all files from stage area to git directory.'
# [main bc217de] Commit all files from stage area to git directory.
#  3 files changed, 19 insertions(+), 1 deletion(-)
#  create mode 100644 capitalize_words.py
#  create mode 100644 rearrange.py
#
# i_yaroshenko@DM-NB-108 MINGW64 ~/checks (main)
# $ git status
# On branch main
# nothing to commit, working tree clean
