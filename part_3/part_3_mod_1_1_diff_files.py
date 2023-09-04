"""Diffing Files"""
# 'diff' command line tool
# take two files or even two directories, and show the differences between them in a few formats.

# We have 2 files rearrange1.py and rearrange2.py which contain two different versions of the same function.
# Diff in '-' in [\w .-]*)

# cat rearrange1.py
#!/usr/bin/env python3

import re


def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .])$", name)
    if result is None:
        return result
    return f'{result[2]} {result[1]}'

# cat rearrange2.py
#!/usr/bin/env python3

import re


def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-])$", name)
    if result is None:
        return result
    return f'{result[2]} {result[1]}'

# diff rearrange1.py rearrange2.py
# open diff_example.png

# other example
# open diff_validations.png

# Explanation:
# The section that starts with '5c5,6' shows a line in the first file that was replaced by two different lines in the
# second file. The number at the beginning of this section indicates the line number in the first and second files.
# The 'c' in between the numbers means that a line was changed.
# The 'section that starts with '11a13,15' shows three lines that are new in the second file.
# The a' stands for added, but that block looks a bit strange.

# Use the '-u' flag to tell diff to show the differences in another format.
# diff -u rearrange1.py rearrange2.py
# open diff_example_u.png

# Explanation:
# It shows the change lines together with some context, using - to mark lines removed, and + to mark lines added.
# We can see that the new file actually has a completely new if block that's part of a chain of conditionals that looks
# very similar, and that's why with the diff output that we saw before, it was confusing which lines had been added.

# wdiff
# highlights the words that have changed in a file instead of working line by line like diff does.

# There are a bunch of graphical tools that display files side by side and highlight the differences by using color.
# Some examples of this include: meld, KDiff3, or vimdiff.

# vimdiff highlights the words that changed in a file by color, in addition to working line by line
