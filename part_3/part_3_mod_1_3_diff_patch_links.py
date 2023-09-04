"""Practical Application of diff and patch"""
# A colleague is asking our help with fixing a script named disk_usage.py.
# The goal of the script is to check how much disk space is currently used, and print an error if it's too little space
# for normal operation. But the script is currently broken because it has a few bugs.

# Make a couple copies of the script
# Add _original to one copy, which we’ll keep unmodified and use for comparison and _fixed to the other copy, which
# we’ll use to repair our fix.

# cp disc_usage.py disc_usage_original.py
# cp disc_usage.py disc_usage_fixed.py

# open disc_usage_fixed.py
# disc_usage_first_execution.png

# After fixing bug we need to get .diff file anf patch it

# generate diff file:
# diff -u disc_usage_original.py disc_usage_fixed.py > disc_usage.diff

# observe disc_usage.diff: cat disc_usage.diff
# open disc_usage_diff.png

# patch
# patch disc_usage.py < disk_usage.diff

# Output:
# patching file disc_usage.py

# Execute script to be sure it works:
# ./disc_usage.py


"""diff and patch Cheat Sheet"""
# There are some other interesting patch and diff commands such as patch -p1, diff -r !

# https://man7.org/linux/man-pages/man1/diff.1.html

# https://man7.org/linux/man-pages/man1/patch.1.html
