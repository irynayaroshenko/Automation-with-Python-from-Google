"""Qwiklabs Assessment: Introduction to Github"""
# Introduction
# In this lab, you'll practice the basics of interacting with GitHub. You'll practice setting up an account,
# logging in, creating a repository, making changes on the local machine, and pushing changes back to the remote
# repository. We use these git operations to share changes from the remote repository to the local repository and
# vice-versa.
#
# What you'll do
# - Create a Github account
# - Create a git repository
# - Git clone to create a local copy on your local machine
# - Add a file to this repository
# - Create snapshot/snapshots of the local repository
# - Push the snapshots to the master branch

# Find description of this Qwiklab in internet.


# Operations and Output from VM terminal during lab:

# student-04-d15b84caed78@linux-instance:~$ git clone https://github.com/irynayaroshenko/Qwiklab_GitHub.git
# Cloning into 'Qwiklab_GitHub'...
# remote: Enumerating objects: 3, done.
# remote: Counting objects: 100% (3/3), done.
# remote: Compressing objects: 100% (2/2), done.
# remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
# Receiving objects: 100% (3/3), done.
# student-04-d15b84caed78@linux-instance:~$ ls -l
# total 4
# drwxr-xr-x 3 student-04-d15b84caed78 google-sudoers 4096 Jul  9 19:19 Qwiklab_GitHub
# student-04-d15b84caed78@linux-instance:~$ cd Qwiklab_GitHub/
# student-04-d15b84caed78@linux-instance:~/Qwiklab_GitHub$ ls -l
# total 4
# -rw-r--r-- 1 student-04-d15b84caed78 google-sudoers 62 Jul  9 19:19 README.md
# student-04-d15b84caed78@linux-instance:~/Qwiklab_GitHub$ ls -al
# total 16
# drwxr-xr-x 3 student-04-d15b84caed78 google-sudoers 4096 Jul  9 19:19 .
# drwxr-xr-x 3 student-04-d15b84caed78 google-sudoers 4096 Jul  9 19:19 ..
# drwxr-xr-x 8 student-04-d15b84caed78 google-sudoers 4096 Jul  9 19:21 .git
# -rw-r--r-- 1 student-04-d15b84caed78 google-sudoers   62 Jul  9 19:19 README.md
# student-04-d15b84caed78@linux-instance:~/Qwiklab_GitHub$ git config --global user.name "student-04-d15b84caed78"
# student-04-d15b84caed78@linux-instance:~/Qwiklab_GitHub$ git config --global user.email "student-04-d15b84caed78@34.135.240.186"
# student-04-d15b84caed78@linux-instance:~/Qwiklab_GitHub$ nano README.md
# student-04-d15b84caed78@linux-instance:~/Qwiklab_GitHub$ git status
# On branch main
# Your branch is up to date with 'origin/main'.
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
#         modified:   README.md
#
# no changes added to commit (use "git add" and/or "git commit -a")
# student-04-d15b84caed78@linux-instance:~/Qwiklab_GitHub$ git add README.md
# student-04-d15b84caed78@linux-instance:~/Qwiklab_GitHub$ git status
# On branch main
# Your branch is up to date with 'origin/main'.
#
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         modified:   README.md
#
# student-04-d15b84caed78@linux-instance:~/Qwiklab_GitHub$ git commit -m "I am editing the README file."
# [main 3af6628] I am editing the README file.
#  1 file changed, 1 insertion(+)
# student-04-d15b84caed78@linux-instance:~/Qwiklab_GitHub$ git push origin main
# Username for 'https://github.com': irynayaroshenko
# Password for 'https://irynayaroshenko@github.com':
# Enumerating objects: 5, done.
# Counting objects: 100% (5/5), done.
# Compressing objects: 100% (2/2), done.
# Writing objects: 100% (3/3), 385 bytes | 385.00 KiB/s, done.
# Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
# To https://github.com/irynayaroshenko/Qwiklab_GitHub.git
#    2ebd7b4..3af6628  main -> main
# student-04-d15b84caed78@linux-instance:~/Qwiklab_GitHub$ nano example.py
# student-04-d15b84caed78@linux-instance:~/Qwiklab_GitHub$ git add example.py
# student-04-d15b84caed78@linux-instance:~/Qwiklab_GitHub$ git commit -m "Add example.py file"
# [main 481e7f8] Add example.py file
#  1 file changed, 3 insertions(+)
#  create mode 100644 example.py
# student-04-d15b84caed78@linux-instance:~/Qwiklab_GitHub$ git push origin main
# Username for 'https://github.com': irynayaroshenko
# Password for 'https://irynayaroshenko@github.com':
# To https://github.com/irynayaroshenko/Qwiklab_GitHub.git
#  ! [rejected]        main -> main (fetch first)
# error: failed to push some refs to 'https://github.com/irynayaroshenko/Qwiklab_GitHub.git'
# hint: Updates were rejected because the remote contains work that you do
# hint: not have locally. This is usually caused by another repository pushing
# hint: to the same ref. You may want to first integrate the remote changes
# hint: (e.g., 'git pull ...') before pushing again.
# hint: See the 'Note about fast-forwards' in 'git push --help' for details.
# student-04-d15b84caed78@linux-instance:~/Qwiklab_GitHub$ git pull origin main
# hint: Pulling without specifying how to reconcile divergent branches is
# hint: discouraged. You can squelch this message by running one of the following
# hint: commands sometime before your next pull:
# hint:
# hint:   git config pull.rebase false  # merge (the default strategy)
# hint:   git config pull.rebase true   # rebase
# hint:   git config pull.ff only       # fast-forward only
# hint:
# hint: You can replace "git config" with "git config --global" to set a default
# hint: preference for all repositories. You can also pass --rebase, --no-rebase,
# hint: or --ff-only on the command line to override the configured default per
# hint: invocation.
# remote: Enumerating objects: 4, done.
# remote: Counting objects: 100% (4/4), done.
# remote: Compressing objects: 100% (2/2), done.
# remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
# Unpacking objects: 100% (3/3), 677 bytes | 677.00 KiB/s, done.
# From https://github.com/irynayaroshenko/Qwiklab_GitHub
#  * branch            main       -> FETCH_HEAD
#    3af6628..aff7b90  main       -> origin/main
# Merge made by the 'recursive' strategy.
#  web_file | 1 +
#  1 file changed, 1 insertion(+)
#  create mode 100644 web_file
# student-04-d15b84caed78@linux-instance:~/Qwiklab_GitHub$ git push origin main
# Username for 'https://github.com': irynayaroshenko
# Password for 'https://irynayaroshenko@github.com':
# Enumerating objects: 7, done.
# Counting objects: 100% (7/7), done.
# Compressing objects: 100% (5/5), done.
# Writing objects: 100% (5/5), 661 bytes | 661.00 KiB/s, done.
# Total 5 (delta 1), reused 0 (delta 0), pack-reused 0
# remote: Resolving deltas: 100% (1/1), done.
# To https://github.com/irynayaroshenko/Qwiklab_GitHub.git
#    aff7b90..18b1c2f  main -> main
# student-04-d15b84caed78@linux-instance:~/Qwiklab_GitHub$