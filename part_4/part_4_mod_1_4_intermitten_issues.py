"""Dealing with Intermittent Issues"""
# intermittent - occurring at irregular intervals; not continuous or steady

# Occasionally bugs, not 100% reproduce. What to do?

# 1. Get more info
# For example, added more logging information to the service (e.g., around the inputs and the function calls that you
# suspect could be involved).
# If you can't modify the code of the program to get more information, check if there's a logging configuration
# that you can change.
# Use DEBUG mode.

# Depending on what the problem is, you might want to look at different sources of information:
# a) load on the computer
# b) processes running at the same time
# c) usage of the network, and so on.

# For bugs that occur at random times, we need to prepare our system to give us as much information as possible when the
# bug happens. This might require several iterations until we get enough information to understand the issue.

"""Heisenbug"""

# Sometimes, the bug goes away when we add extra logging information, or when we follow the code step by step using a
# debugger. This is an especially annoying type of intermittent issue, nicknamed 'Heisenbug', in honor of Werner
# Heisenberg. He's the scientist that first described the observer effect, where just observing a phenomenon alters the
# phenomenon.
# Heisenbugs are extra hard to understand, because when we meddle (interfere in smth) with them, the bug goes away.
# These bugs usually point to bad resource management. Maybe the memory was wrongly allocated, the network connections
# weren't correctly initialized, or the open files weren't properly handled.
# In these cases, we usually need to just spend time looking at the effected code until we finally figure out what's up.

"""Restart solution"""
# Yet another type of intermittent issue is the one that goes away when we turn something off and on again.
# When we reboot a computer or restart a program, a bunch of things change. Going back to a clean slate means releasing
# all allocated memory, deleting temporary files, resetting the running state of programs, re-establishing network
# connections, closing open files and more.
# If a problem goes away by turning it off and on again, there's almost certainly a bug in the software, and the bug
# probably has to do with not managing resources correctly.
# So if an issue goes away after a restart, it's a good idea to try to figure out why that is, and see if it's possible
# to fix it in a way that doesn't require turning it off and on again. If in the end, we can't find the actual reason,
# scheduling a restart at a time that's not problematic can also be an option.

