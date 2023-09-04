"""Parallelizing Operations"""
# Reading information from disk or transferring it over the network is a slow operation. In typical scripts while
# this operation is going on, nothing else happens. The script is blocked, waiting for input or output while the CPU
# sits idle. One way we can make this better is to do operations in parallel.
# That way, while the computer is waiting for the slow IO, other work can take place. The tricky part is dividing up
# the tasks so that we get the same result in the end.

# There's actually a whole field of computer science called 'Concurrency', dedicated to how we write programs that do
# operations in parallel.

# Our OS handles many processes that run on our computer. If a computer has more than one core, the operating system
# can decide which processes get executed on which core, and no matter the split between cores, all of these processes
# will be executing in parallel. Each of them has its own memory allocation and does its own IO calls.

# The OS will decide what fraction of CPU time each process gets and switch between them as needed. So a very easy way
# to run operations in parallel is just to split them across different processes, calling your script many times each
# with a different input set, and just let the operating system handle the concurrency.

# Let's say you want to collect statistics on the current load and memory usage for all the computers in your network.
# You can do this by writing a script that connects to each computer in a list and gets the stats.
# Each connection takes a while to complete, so the total run-time of the script would be the sum of the time taken by
# all those connections.
# Instead, you could split the list of computers into smaller groups and use the OS to call the script many times once
# for each group. That way, the connections to the different computers can be started in parallel, which minimizes the
# time but the CPU isn't doing anything.
# This is super easy to do, and for many scripts, it'll be the right choice.

# Another easy thing to do, is to have a good balance of different workloads that you run on a computer.
# If you have a process that's using a lot of CPU while a different process is using a lot of network IO and
# another process is using a lot of disk IO, these can all run in parallel without interfering with each other.

# When using the OS to split the work and the processes, these processes don't share any memory, and sometimes we might
# need to have some shared data. In that case, we'd use threads.

# Threads let us run parallel tasks inside a process.
# This allows threats to share some memory with other threads in the same process. Since this isn't handled by the OS,
# we'll need to modify our code to create and handle the threats.

# For that, we'll need to look into how the programming language we're using implements threading.
# In Python, we can use the Threading or AsyncIO modules to do this. These modules let us specify which parts of the
# code we want to run in separate threads or as separate asynchronous events, and how we want the results of
# each to be combined in the end.

# One thing to watch out for is that depending on the actual threading implementation for the language you're using,
# it might happen that all threads get executed in the same CPU processor. In that case, if you want to use more
# processors, you'll need to split the code into fully separate processes.
# If your script is mostly just waiting on input or output, also known as I/O bound, it might matter if it's
# executed on one processor or eight. But you might be doing this in parallel because you're using all of the available
# CPU time. In other words, your script is CPU bound.
# In this case, you'll definitely want to split your execution across processors.

# Now there's a point where adding more parallel processes means things become even slower, not faster.
# If we're trying to read a bunch of files from disk and do too many operations in parallel, the disk might end up
# spending more time going from one position to another than actually retrieving the data, or if we're doing a ton of
# operations that use a lot of CPU, the OS could spend more time switching between them than actually making progress
# in the calculations we're trying to do.

# So when doing operations in parallel, we need to find the right balance of simultaneous actions that let
# our computers stay busy without starving our system for resources.

# I recently felt the benefits of applying concurrency.
# I was working on migrating data that was stored in one format, and I needed to store it in a different format.
# There were a lot of gigabytes of data that needed migrating, so of course I wasn't going to do it manually.
# My first version of the script was taking an average of one hour per gigabyte migrated.

# This was much slower than I expected, so I decided to spend more time tweaking the code to make the migration go
# faster. I reorganized the logic to have a separate thread per file which decreased the total time to work through the
# files since it now wasn't a linear process, and then, to make it go even faster, I split the work onto different
# machines, each running a bunch of threads.
# After all this rearranging to use the resources I have, I brought it down to three minutes per gigabyte.
