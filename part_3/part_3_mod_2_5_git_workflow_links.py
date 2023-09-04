"""The Basic Git Workflow"""
# !! All the files we want to manage with Git must be a part of a Git repository !!

# We initialize a new repository by running the 'git init' command in ANY file system directory and now Git repository
# can be used to track changes to files inside this dir.


# check current git configuration:
# git config -l

# $ git config -l
# diff.astextplain.textconv=astextplain
# filter.lfs.clean=git-lfs clean -- %f
# filter.lfs.smudge=git-lfs smudge -- %f
# filter.lfs.process=git-lfs filter-process
# filter.lfs.required=true
# http.sslbackend=openssl
# http.sslcainfo=C:/Program Files/Git/mingw64/etc/ssl/certs/ca-bundle.crt
# core.autocrlf=true
# core.fscache=true
# core.symlinks=false
# core.editor=nano.exe
# pull.rebase=false
# credential.helper=manager
# credential.https://dev.azure.com.usehttppath=true
# init.defaultbranch=main
# user.name=ira_yar                        **
# user.email=irina.yaroshenko99@gmail.com  **
# core.repositoryformatversion=0
# core.filemode=false
# core.bare=false
# core.logallrefupdates=true
# core.symlinks=false
# core.ignorecase=true

# ** This information will appear in public commit logs if you use a shared repository.

# create <file>
# git add <file>  (in order git to track it)
# file modified
# git add <file>  (update)
# git commit -m "Comment message"


# A commit message is generally broken up into a few sections.
# The 1st line is a short summary of the commit followed by a blank line. This is followed by a full description of
# the changes with details why they're necessary and anything that might be especially interesting about them
# or difficult to understand.

# Commit message is a short description of the change (up to 50 characters), followed by one or more paragraphs giving
# more details of the change (if needed).
# open example_commit.png


# track the log:
# git log

# $ git log
# commit bc217debfad8051d7c0ba567b81ab7e95d2e16b3 (HEAD -> main)
# Author: ira_yar <irina.yaroshenko99@gmail.com>
# Date:   Wed Jul 5 17:12:10 2023 +0300
#
#     Commit all files from stage area to git directory.
#
# commit da5edf10fa733a2152014165cb058aacff75717c
# Author: ira_yar <irina.yaroshenko99@gmail.com>
# Date:   Wed Jul 5 16:12:26 2023 +0300
#
#     First file added to test git repo


# Links
# 1) https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/process/submitting-patches.rst?id=HEAD
# 2) https://commit.style/
# 3) https://thoughtbot.com/blog/5-useful-tips-for-a-better-commit-message
# 4) https://help.github.com/en/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address

