"""What is binary search?"""
# Linear search works for searching in the list but the longer the list, the longer it can take. In other words, the
# time it takes to find the result is proportional to the length of the list.
# If the list is sorted, we can use an alternative algorithm for searching called binary search.
# Because the list is sorted, we can make decisions about the position of the elements in the list.
# This is calculated as the base two logarithm of the list length, and the benefits get more and more
# significant the longer the list.

# For a list of 100,000 elements, it would be 17 comparisons instead of 100,000 comparisons.
# But remember, that for this to work, the list needs to be sorted. If it's not, we would need to sort it first,
# which takes a chunk of time.
# It can still make sense to do it if we're going to search through it several times, but it doesn't make sense to sort
# the list and then use binary search to only find one element. In that case, using linear search is simpler and faster.

# Linear and binary search implementations in Python:
def linear_search(list, key):
    """If key is in the list returns its position in the list, otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1


def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1

"""Applying Binary Search in Troubleshooting"""

# Cases:

# In troubleshooting, we can apply binary search when we need to go through and test a long list of hypotheses.
# When doing this, the list of elements contains all the possible causes of the problem, and we keep reducing the
# problem by half until only one option is left.
# The list of elements could be: entries in a file, extensions enabled, boards connected to a server, or even lines of
# code added to a faulty release.
# With each iteration, the problem is cut in half. This approach is sometimes called 'bisecting' - means dividing in 2.

# 1.
# In an earlier video, we gave the example of a new version of a program that fail to start when the old configuration
# directory was present. If the directory contained a bunch of different files in it, we could identify the one causing
# the failure by bisecting the list of files.

# Say the old directory contained 12 different config files. To identify which of those 12 is causing the failure, we
# can create a copy of the directory with just 6 of the 12 files and then try to start the program again.
# If it crashes, then the bad file is among those 6 files. If it doesn't, it's among the other six.
# In the next step, we would pick 3 out of the failing group of 6.
# If the program crashes again, it's 1 of those 3.
# If it doesn't, it's 1 of the other 3.
# For the last 3, we can first check 2 together or just go 1 by 1.
# Either way, it's two checks to get to the failing file.
# This means that with a total of 4 attempts, we can find out which of the 12 files is causing the problem.

# After that, we can proceed in the same way with the contents of that single file, cutting it in half repeatedly,
# until we find the specific part of the file that's causing the problem.

# 2.
# The same process can be applied to a large variety of problems.
# It's very common for example to use it to figure out which browser extension is causing the browser to crash,
# disabling half of the extensions then checking if the browser crashes with that subset and so on until we find the
# faulty extension.

# 3.
# We can also use this technique to discover which plug-in in a desktop environment is causing the computer to run out
# of memory, or which entry in a database is causing the program to raise an exception.

# 4.
# We can also apply this to code when trying to find a bug that was introduced in a recent version.
# If we know the list of changes that were made between one version and the next, we can keep cutting that list in half
# until we find the one that caused the failure.

# 5. git bisect  https://git-scm.com/docs/git-bisect
# When using Git for version control, we can use a Git command called 'bisect'.
# Bisect receives two points in time in the Git history and repeatedly lets us try the code at the middle point between
# them until we find the commit that caused the breakage. This doesn't even need to be your Git repository. If you're
# using open source software that's tracking Git, you can use bisect commit to find out which command cause the software
# to stop working on your computer.
# For example, if the latest release of the Linux kernel causes the soundcard on your computer to stop working, you can
# use 'git bisect' to find the commit that broke it and report this as a bug to be fixed.

# The longer the list of items that needs to be checked, the more we'll gain by cutting our problem in half on each
# iteration. If it's just 5 options that need to be checked, we can simply go one-by-one. But if it's a 100, we
# definitely want to bisect the problem, so we can find the answer in seven steps. Not a 100.

# Depending on what the problem is, it might make sense to spend some time creating a script that checks for the issue.
