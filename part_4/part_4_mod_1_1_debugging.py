# All course videos: https://www.youtube.com/playlist?list=PLP8aFdeDk9g4ImMVv0PwgTl7ztwBZryi0

"""What is debugging?"""
# Troubleshooting is the process of identifying, analyzing, and solving problems.
# Debugging is the process of identifying, analyzing, and removing bugs in a system.

# Generally, we say troubleshooting when we're fixing problems in the system running the application, and
# debugging when we're fixing the bugs in the actual code of the application.

# Tools like 'tcpdump' and 'Wireshark' can show us ongoing network connections, and help us analyze the traffic going
# over our cables.
# Tools like 'ps', 'top', or 'free' can show us the number and types of resources used in the system.
# We can use a tool like 'strace' to look at the system calls made by a program, or 'ltrace' to look at the library
# calls made by the software.

# Debuggers let us follow the code line by line, inspect changes in variable assignments, interrupt the program when a
# specific condition is met, and more.

"""Problem Solving Steps"""
# 1. Gather information. Get reproduction case - a clear description of how and when the problem appears.
# 2. Finding the root cause of the problem
# 3. Performing the necessary remediation (fixing things that aren't right), e.g. revert to working copy, fix problem,
# write tests and add it to CI, commit problem solution to project

# Sometimes we can understand the problem just enough to create a workaround that lets our users get back to work
# quickly, but we'd still need more time to get to the root cause and prevent the problem from happening again.

# Throughout the whole process, it's important that we document what we do. We should note down the info that we get,
# the different things we tested to try, and figure out the root cause. And the steps we took to fix the issue.

# Long-term remediation can be deploying monitoring on problem area or computer to make sure you get notified early in
# the future.

"""Silently Crashing Application"""
# Say a user contacts us to let us know that a certain application fails to open.
# As we said earlier, the first thing to do is to get more information about the conditions that caused the failure.
# What the error is that the user is getting and then check if we experience the same failure.

# By asking for these details, we discover that a new version of the software was recently released.
# And when we upgrade to this new version, we can reproduce the problem on our own computer like this:

# on video just run program: ./purplebox.py


# We see that when we try to run the program it prints no error at all.
# It just exits immediately.

# We need to figure out what's going on. Even if there's no error message.

# There are a bunch of tools that can help us better understand what's going on with the system and with our
# applications. With the help of these tools, we can extend our knowledge of a particular problem view the actions of
# the program from a different point of view and get the info we need.

# Among these tools 'strace' lets us look more deeply at what the program is doing. It will trace a system calls made
# by the program and tell us what the result of each of these calls was.

# So to figure out what's up with our program that's failing to open will s trace the failing application:

# strace ./purplebox.py


# Output of 'strace' command shows us all the system calls are program made.

# System calls are the calls that the programs running on our computer make to the running kernel.
# There are lots of different system calls and depending on what we're trying to debug.

# If you want to understand what these system calls are, you can read more about each of them in the corresponding
# manual pages.

# To make 'strace' output more manageable:

# strace -o <file_name_where_to_write> <program>
# Example: strace -o failure.strace ./purplebox.py


# -o  - store the output into a file and then browse the contents of that file. It lets us refer back to the file later
# if we need to.

# (Or 'less' without writing to the file: strace ./script.py | less)


# Open generated file with 'less'. We go to the end of the file pressing Shift+G then scroll up to see if we find
# anything suspicious.

# less <file_name>
# Example: less failure.strace

# (Also, we can pipe the output to the 'less' command which we could use to scroll through a lot of texts.)


# !!! open cause_of_issue.png

# Close to the end of the log we can see that the application tries to open a directory called .config/purplebox,
# which doesn't exist.
# Let's look at this line in a bit more detail.

# The name of the system call is 'openat', it's one of the calls used to open files or directories.
# The content of the call shows the parameters passed including the path
# that's being opened ("/home/user/.config/purplebox") and a bunch of flags (O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY).
# In particular the 'O_DIRECTORY' flag tells us that the program is trying to open this path as a directory.
# The number after the equal sign (-1) shows us the return code of the sys call.

# So the program is trying to open this directory, and it turns out it doesn't exist. Since this is happening shortly
# before the program finishes it's a likely candidate for the root cause of the issue.
# For checking this assumption let's create the directory and try to start the program again.

# mkdir ~/.config/purplebox
# ./purplebox.py

# Program works (open purplebox.png)

# Thus, root cause of the program - missing directory.

# What to do next?
# The immediate remediation is to tell the user to create the directory so that he can get back to work quickly.
# The long-term remediation is to contact the developers of the software to let them know that the program will fail
# to start if the director is missing.
# This gives them a heads-up about the problem, so they can fix it in the next version.

# And what about the documentation? - We should note that this version of the software won't start if that directory
# doesn't exist.
# That will help others facing the same issue to quickly find out the solution.

