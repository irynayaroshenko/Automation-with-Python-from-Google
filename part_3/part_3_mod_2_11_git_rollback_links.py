"""Rollbacks. Revert PREVIOUS commit"""

# There are a few ways to rollback commits in Git. For now, we'll focus on using the 'git revert' command which doesn't
# just mean undo. Instead, it creates a commit that contains the inverse of all the changes made in the bad commit in
# order to cancel them out.

# For example, if a particular line was added in the bad commit, then in the reverted commit, the same line will be
# deleted.
# This way you get the effect of having undone the changes, but the history of the commits in the project remains
# consistent leaving a record of exactly what happened. So 'git revert' will create a new commit, that is the opposite
# of everything in the given commit.

# We can revert the latest commit by using the HEAD alias that we mentioned before.
# Since we can think of HEAD as a pointer to the snapshot of your current commit, when we pass HEAD to the revert
# command we tell Git to rewind that current commit.
# Shortly, with 'git revert', a new commit is created with inverse changes. This cancels previous changes instead of
# making it as though the original commit never happened.

# git revert HEAD


# Since a revert is a normal commit, we can see both the commit and the reverted commit in the log.

# Example:

# [main 4f1bde0] Revert "Test file added"
#  1 file changed, 0 insertions(+), 0 deletions(-)
#  delete mode 100644 test_file_for_revert.txt


# Observe 2 last commits (-p - patch created by the commit, -2 - limits the output to the last two entries):

# git log -p -2


# $ git log -p -2
# commit 4f1bde05d6f088edc99be018520022795e5340e7 (HEAD -> main)
# Author: ira_yar <irina.yaroshenko99@gmail.com>
# Date:   Fri Jul 7 12:56:38 2023 +0300
#
#     Revert "Test file added"
#
#     This reverts commit 86d7c5b05264996e46406e1419ab7b0a01651ec9.
#
# diff --git a/test_file_for_revert.txt b/test_file_for_revert.txt
# deleted file mode 100644
# index e69de29..0000000
#
# commit 86d7c5b05264996e46406e1419ab7b0a01651ec9
# Author: ira_yar <irina.yaroshenko99@gmail.com>
# Date:   Fri Jul 7 12:55:57 2023 +0300
#
#     Test file added
#
# diff --git a/test_file_for_revert.txt b/test_file_for_revert.txt
# new file mode 100644
# index 0000000..e69de29

"""Identifying a Commit and Revert"""

# observe last 2 commits in log. Copy commit ID you want to revert:

# git log -2


# revert commit with commit ID (window for message will be opened):

# git revert 03d98f144d252485eceda068b122a4319adfbbdc



# $ git log -2
# commit 4f1bde05d6f088edc99be018520022795e5340e7 (HEAD -> main)
# Author: ira_yar <irina.yaroshenko99@gmail.com>
# Date:   Fri Jul 7 12:56:38 2023 +0300
#
#     Revert "Test file added"
#
#     This reverts commit 86d7c5b05264996e46406e1419ab7b0a01651ec9.
#
# commit 86d7c5b05264996e46406e1419ab7b0a01651ec9
# Author: ira_yar <irina.yaroshenko99@gmail.com>
# Date:   Fri Jul 7 12:55:57 2023 +0300
#
#     Test file added

# 4f1bde05d6f088edc99be018520022795e5340e7 - commit ID 40 chars long, it's Hash, which is calculated using an algorithm
# called SHA1. (Essentially, what this algorithm does is take a bunch of data as input and produce a 40 character
# string from the data as the output. In the case of Git, the input is all information related to the commit, and
# the 40 character string is the commit ID.)

# Why Git uses a hash instead of a counter, and how that hash is computed?
# Although SHA1 is part of the class of cryptographic Hash functions, Git doesn't really use these hashes for security.
# Instead, they're used to guarantee the consistency of our repository.

# Having consistent data means that we get exactly what we expect.
# To quote Git's creator, Linus Torvalds, you can verify the data you get back out is the exact same data you put in.
# This is really useful in distributed systems like Git because everyone has their own repository and is transmitting
# their own pieces of data. Computing the hash keeps data consistent because it's calculated from all the information
# that makes up a commit: commit message, date, author, and the snapshot taken of the working tree.
# The chance of 2 different commits producing the same hash, commonly referred to as a collision, is extremely tiny.
# So small, it wouldn't happen by chance. It'd take a lot of processing power to cause this to happen on purpose.
# If you use a hash to guarantee consistency, you can't change anything in the Git commit without the SHA1 hash changing
# too. Remember our discussion about fixing commits with the --amend command?
# Each time we amend a commit, the commit ID will change.
# This is why it's important not to use --amend on commits that have been made public.

# The data integrity offered by the commit ID means that if a bad disk or network link corrupt some data in your
# repository, or worse, if someone intentionally corrupt some data, Git can use the hash to spot that corruption: the
# data you've got isn't the data you expected, something went wrong.


# Reverting example ([main 4592ff8] - first symbols of commit. To check use 'git show 4592ff8'):

# git revert 4592ff8541b7eaece6e3fae2c5d1692d949ab029
# [main 4592ff8] Revert "Remaning file"
#  1 file changed, 0 insertions(+), 0 deletions(-)
#  rename all_checks_correct.py => all_checks.py (100%)


# Shows one or more objects (blobs, trees, tags and commits). This is equivalent to running 'git show HEAD'.
# The output provides a combined diff format. It tells us the commit details of the HEAD commit, along with a textual
# diff of the changes included in that commit. This can be useful when you want a 'git diff' output in addition to the
# commit info supplied by 'git log'.

# git show


"""Git Revert Cheat Sheet"""

# 'git checkout' is effectively used to switch branches
# https://git-scm.com/docs/git-checkout

# 'git reset' basically resets the repo, throwing away some changes
# https://git-scm.com/docs/git-reset#_examples

# There are some other useful articles online, which discuss more aggressive approaches to resetting the repo
# https://jwiegley.github.io/git-from-the-bottom-up/3-Reset/4-doing-a-hard-reset.html

# 'git commit --amend' is used to make changes to commits after-the-fact, which can be useful for making notes about
# a given commit.
# https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---amend

# git revert makes a new commit which effectively rolls back a previous commit. It’s a bit like an undo command.
# https://git-scm.com/docs/git-revert


# There are a few ways you can rollback commits in Git.
# https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things

# There are some interesting considerations about how git object data is stored, such as the usage of sha-1.
# https://en.wikipedia.org/wiki/SHA-1
# https://github.blog/2017-03-20-sha-1-collision-detection-on-github-com/
