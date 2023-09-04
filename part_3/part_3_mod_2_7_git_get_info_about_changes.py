"""Getting More Information About Our Changes"""
# -p stands for 'patch'. Gives full info about changes in files. 'q' to exit.

# git log -p
# git log -p -2  (2 last commits)


# The format is equivalent to the diff-u output. It shows added lines with + and remove lines with -. Git automatically
# uses a paging tool that allows us to scroll using page up, page down, and the arrow keys.
# We still have one commit below the other, but now each commit takes up a different amount of space,
# depending on how many lines were added or removed in that commit.

# Example:
# commit bc217debfad8051d7c0ba567b81ab7e95d2e16b3
# Author: ira_yar <irina.yaroshenko99@gmail.com>
# Date:   Wed Jul 5 17:12:10 2023 +0300
#
#     Commit all files from stage area to git directory.
#
# diff --git a/capitalize_words.py b/capitalize_words.py
# new file mode 100644
# index 0000000..8bf00a9
# --- /dev/null
# +++ b/capitalize_words.py
# @@ -0,0 +1,8 @@
# +#!/usr/bin/env python
# +
# +import sys
# +
# +
# +for line in sys.stdin:
# +    words = line.strip().split()
# +    print(" ".join([word.capitalize() for word in words]))
# diff --git a/disc_usage_fixed.py b/disc_usage_fixed.py
# index 90b6b0e..0cc5816 100644
# --- a/disc_usage_fixed.py
# +++ b/disc_usage_fixed.py
# @@ -85,7 +85,7 @@ if not check_disk_usage('/', 2, 10):  # changes made
#      print("ERROR: No enough space disc.")
#      sys.exit(1)
#
# -print('Everything ok.')
# +print('Everything ok!')
#  sys.exit(0)
#
#  # after execution: ./disc_usage_fixed.py
# diff --git a/rearrange.py b/rearrange.py
# new file mode 100644
# index 0000000..7783044
# --- /dev/null
# +++ b/rearrange.py
# @@ -0,0 +1,10 @@
# +import re
# +
# +
# +def rearrange_name(name):
# +    result = re.search(r'^([\w .]*), ([\w .]*)$', name)
# +    if result is None:
# +        return name
# +    return f'{result[2]} {result[1]}'
# +
# +# print(rearrange_name('Yaroshenko, Iryna'))
# \ No newline at end of file

# If we don't wand to scroll all the commits until we find the commit that we're actually interested in, another option
# is to use the git show command.
# This command takes a commit ID (e.g. bc217debfad8051d7c0ba567b81ab7e95d2e16b3) as a parameter,
# and will display the information about the commit and the associated patch.

# git show <commit ID>
# git show bc217debfad8051d7c0ba567b81ab7e95d2e16b3


# show some stats about the changes in the commit: which files were changed and how many lines were added or removed.

# git log --stat


# Example:
# i_yaroshenko@DM-NB-108 MINGW64 ~/checks (main)
# $ git log --stat
# commit 2ce41b541e84d3da6848cae63a81890e9d55bd9d (HEAD -> main)
# Author: ira_yar <irina.yaroshenko99@gmail.com>
# Date:   Thu Jul 6 20:51:02 2023 +0300
#
#     Commit without staging modified file all_checks.py
#
#  all_checks.py | 14 ++++++++++++++
#  1 file changed, 14 insertions(+)
#
# commit bc217debfad8051d7c0ba567b81ab7e95d2e16b3
# Author: ira_yar <irina.yaroshenko99@gmail.com>
# Date:   Wed Jul 5 17:12:10 2023 +0300
#
#     Commit all files from stage area to git directory.
#
#  capitalize_words.py |  8 ++++++++
#  disc_usage_fixed.py |  2 +-
#  rearrange.py        | 10 ++++++++++
#  3 files changed, 19 insertions(+), 1 deletion(-)
#
# commit da5edf10fa733a2152014165cb058aacff75717c
# Author: ira_yar <irina.yaroshenko99@gmail.com>
# Date:   Wed Jul 5 16:12:26 2023 +0300
#
#     First file added to test git repo
#
#  disc_usage_fixed.py | 95 +++++++++++++++++++++++++++++++++++++++++++++++++++++
#  1 file changed, 95 insertions(+)

# if we don't remember all changes we made, use 'diff'. This format is equivalent to the 'diff -u' output

# git diff



# Example:
# $ git diff
# warning: in the working copy of 'all_checks.py', LF will be replaced by CRLF the next time Git touches it
# diff --git a/all_checks.py b/all_checks.py
# index cfb40a6..3463a71 100644
# --- a/all_checks.py
# +++ b/all_checks.py
# @@ -9,6 +9,8 @@ def main():
#    if check_reboot():
#      print("Pending Reboot")
#      sys.exit(1)
# +  print("Everything ok.")
# +  sys.exit(0)
#
#  main()

# If our change was bigger and included several files, we could pass a file by parameter to see the differences
# relevant to that specific file instead of all the files at the same time.

# git diff <file_name>


# Git will show us the change being added and ask us if we want to stage it or not.

# git add -p


# Example:
# $ git add -p
# warning: in the working copy of 'all_checks.py', LF will be replaced by CRLF the next time Git touches it
# warning: in the working copy of 'all_checks.py', LF will be replaced by CRLF the next time Git touches it
# diff --git a/all_checks.py b/all_checks.py
# index cfb40a6..3463a71 100644
# --- a/all_checks.py
# +++ b/all_checks.py
# @@ -9,6 +9,8 @@ def main():
#    if check_reboot():
#      print("Pending Reboot")
#      sys.exit(1)
# +  print("Everything ok.")
# +  sys.exit(0)
#
#  main()
#
# (1/1) Stage this hunk [y,n,q,a,d,e,?]? y

# If we call 'git diff' again, it won't show any differences, since git diff shows only un-staged changes by default.
# Instead, we can call 'git diff --staged' to see the changes that are staged but not committed.
# With this command, we can see the actual stage changes before we call git commit.

# Example:
# i_yaroshenko@DM-NB-108 MINGW64 ~/checks (main)
# $ git diff
#
# i_yaroshenko@DM-NB-108 MINGW64 ~/checks (main)
# $ git diff --staged
# diff --git a/all_checks.py b/all_checks.py
# index cfb40a6..3463a71 100644
# --- a/all_checks.py
# +++ b/all_checks.py
# @@ -9,6 +9,8 @@ def main():
#    if check_reboot():
#      print("Pending Reboot")
#      sys.exit(1)
# +  print("Everything ok.")
# +  sys.exit(0)
#
#  main()