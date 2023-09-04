"""Debugging a Segmentation Fault"""
# We have a simple example program that crashes with a segfault.
# When an application crashes like this, it's useful to have a core file of the crash:

# ./example
# Output: Segmentation fault

# Core files store all the information related to the crash so that we or someone else can debug what's going on.
# It's like taking a snapshot of the crash when it happens to analyze it later.

# We need to tell the OS that we want to generate those core files.
# We do that by running the 'ulimit' command, then using '-c' flag for core files, and then saying 'unlimited' to state
# that we want core files of any size:

# ulimit -c unlimited

# Once we've done that, we can try executing our example again:

# ./example

# Our crashing program has generated a core file. Let's check it out:

# ls -l.

# open debug_segfault_1.png
# This file contains all the information of what was going on with the program when it crashed.
# We can use it to understand why the program crashed by passing it to the 'gdb' debugger.

# We'll call it 'gdb -c core' to give it a core file and then example to tell it where the executable that crashed is
# located:

# gdb -c core example

# Open debug_segfault_2.png
# When it starts, gdb shows a bunch of messages including its version, license, and how to get help.
# It then tells us that the program finished with a segmentation fault.
# It shows that the crash happened inside the '__strlen_' function in a file that's part of the system libraries.
# The 'No such file or directory' error that we're seeing here means that we don't have the debugging symbols for
# that system library, but that's okay.

# We trust the strlen function to work correctly. It's our code that's buggy.
# Let's look at the full backtrace of the crash by using the 'backtrace' command - shows a summary of the function calls
# that were used to the point where the failure occurs:

# backtrace

# open debug_segfault_3.png
# The first element in the list is the function where the crash occurred. The second element is the function that called
# the function and so on. In this case, we see that the strlen function that failed was called by  copy_parameters()
# function in our code, which was called by the main() function.

# We can use the 'up' command to move to the calling function in the backtrace and check out the line and copy
# parameters that caused the crash:

# up

# open debug_segfault_4.png
# We see that the faulty line is calling the strlen() function, but it's not clear why that would fail.

# We can get more contexts for the code that failed by calling 'list' command that shows the lines around current one:

# list

# open debug_segfault_5.png
# Here, we see a chunk of C code. If this is the first time you look at C code, it might seem a bit confusing.
# That's okay. There are some similarities with Python, but also, some things that are pretty different.
# We see that the faulty line, line 10, is in the body of a for loop.
# The variable that the for loop uses to iterate is called 'i'.
# Let's check out the value of 'i' using the 'print' command:

# print i    (see the same debug_segfault_5.png)

# gdb uses the dollar sign followed by a number to give separate identifiers to each result it prints.
# In this case, the result is 1. In other words, when the crash happened, 'i' had the value of 1.
# Since this variable is being used to access an array called argv, let's print the contents of the first element
# argv[0] and then the second element argv[1]:

# print argv[0]
# print argv[1]

# open debug_segfault_6.png
# What are those weird numbers starting with 0x?
# Those are hexadecimal numbers, and they are used to show addresses in memory where some data is stored.
# Here, GDB is telling us that the first element in the argv array is a pointer pointing to "./example" string.
# The second element is a pointer to zero also known as a Null pointer. open debug_segfault_7.png

# Zero is never a valid pointer. It usually signals the end of data structures in C. So our code is trying to access
# the second element in the array, but the array only has one valid element.

# In other words, the for loop is doing one iteration to many.
# This is known as an 'Off-by-one error', and it's a super common error.
# In this case, the fix is really simple: we need to change '<=' to '<' so that the iteration stops one element before.
# open debug_segfault_8.png

# Crashing with a segmentation fault is common when dealing with applications written in languages like C or C++.
# In Python, we usually need to deal with unexpected exceptions making our program crash.
