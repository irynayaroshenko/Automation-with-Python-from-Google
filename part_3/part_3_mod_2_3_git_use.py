"""First Steps with Git"""
# Configure git:

# git config --global user.email "irina.yaroshenko99@gmail.com"
# git config --global user.name "ira_yar"

# (--global - state that we want to set this value for all git repositories that we'd use)

# to check setup email:
# git config --global user.email


# create new repo (folder 'checks'):
# mkdir checks


# go to new folder:
# cd checks


# initialize an empty git repository in the current directory 'checks':
# git init

# Output:
# Initialized empty Git repository in C:/Users/i_yaroshenko/checks/.git/


# check all files in directory:
# ls -la


# check what's in .git dir:
# ls -l .git

# .git is called a Git directory.
# You can think of it as a database for your Git project that stores the changes and the change history.
# We can see it contains a bunch of different files and directories:
# ls -l .git
# total 7
# -rw-r--r-- 1 i_yaroshenko 1049089  21 Jul  5 15:30 HEAD
# -rw-r--r-- 1 i_yaroshenko 1049089 130 Jul  5 15:30 config
# -rw-r--r-- 1 i_yaroshenko 1049089  73 Jul  5 15:30 description
# drwxr-xr-x 1 i_yaroshenko 1049089   0 Jul  5 15:30 hooks/
# drwxr-xr-x 1 i_yaroshenko 1049089   0 Jul  5 15:30 info/
# drwxr-xr-x 1 i_yaroshenko 1049089   0 Jul  5 15:30 objects/
# drwxr-xr-x 1 i_yaroshenko 1049089   0 Jul  5 15:30 refs/

# We won't touch any of these files directly, we'll always interact with them through Git commands.
# So whenever you clone a repository, this git directory is copied to your computer. Whenever you run 'git init' to
# create a new repository like we just did, a new git directory is initialized.

# The area outside the git directory is the working tree. The working tree is the current version of your project.
# You can think of it like a workbench or a sandbox where you perform all the modification you want to your file.
# This working tree will contain all the files that are currently tracked by Git and any new files that we
# haven't yet added to the list of track files.

# Files that we need/want to add to git should be in repo folder, here 'checks'. When we add files, git track them:
# git add disc_usage_fixed.py

# Now file is in Staging area (or Index)


# check
# git status


# track the log:
# git log


# CORRECTLY copy file to current dir on Windows:
# $ cp /c/pythonProject/Automation\ with\ Python/scripts/rearrange.py .

# How to write files and folders with spaces in names:
# Automation\ with\ Python - system changed this because of spaces in dir name.
# "Automation with Python" - one more way to write name with spaces










