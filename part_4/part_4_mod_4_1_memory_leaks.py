"""Memory Leaks and How to Prevent Them"""
# Most applications need to store data in memory to run successfully. We called that earlier, how processes interact
# with the OS to request chunks of memory, and then release them when they're no longer needed.

# When writing programs in languages like C, or C++, the programmer is in charge of deciding how much memory to request,
# and when to give it back. Since we're human, we might sometimes forget to free memory that isn't in use anymore,
# this is what we call a Memory leak.

# A memory leak, happens when a chunk of memory that's no longer needed is not released.

# If the memory leak is small, we might not even notice it, and it probably won't cause any problems.
# But, when the memory that's leaked becomes larger and larger over time, it can cause the whole system to start
# misbehaving.

# When a program uses a lot of RAM, other programs will need to be swapped out and everything will run slowly.
# If the program uses all the available memory, then no processes will be able to request more memory,
# and things will start failing in weird ways. When this happens, the OS might terminate processes to free up some
# memory, causing unrelated programs to crash.

# You might be thinking why should I care if I don't plan to code in C or C++, it's true, the languages like Python,
# Java, or Go manage memory for us, but things can still go wrong if we don't use the memory correctly.

# To understand how this works, let's look into what these languages do.
# First, they request the necessary memory when we create variables, and then they run a tool called Garbage collector,
# that's in charge of freeing the memory that's no longer in use. To detect when that's the case, the garbage collector
# looks at the variables in use and the memory assigned to them and then checks if there any portions of the memory that
# aren't being referenced by any variables.

# Say for example, you create a dictionary inside a function, use it to process a text file, calculate the frequency of
# the words in the file, and then return the word that was used the most frequently. When the function returns,
# the dictionary is not referenced anymore. So the garbage collector can detect this and give back the unused memory,
# but if the function returns the whole dictionary, then it's still in use, and the memory won't be given
# back until that stops being the case.

# When our code keeps variables pointing to the data in memory, like a variable in the code itself, or an element in a
# list or a dictionary, the garbage collector won't release that memory. In other words, even when the language takes
# care of requesting and releasing the memory for us, we could still see the same effects of a memory leak.

# If that memory keeps growing, the code could cause the computer to run out of memory, just like a memory leak would.
# The OS will normally release any memory assigned to a process once the process finishes.
# So memory leaks are less of an issue for programs that are short-lived, but can become especially problematic for
# processes that keep running in the background.

# Even worse than these, are memory leaks caused by a device driver, or the OS itself.
# In these cases, only a full restart of the system releases the memory.

# Say you notice that your computer seems to run out of memory a lot, you look at the running programs over the course
# of some time, and realize that there's a process that keeps using more and more memory as the hours pass.
# If you reset that process, it begins with a very small amount of memory, but quickly requires more and more.
# If that's the case, it's pretty likely that this program has a memory leak.

# What can we do if we suspect a program has a memory leak?

# We can use a memory profiler to figure out how the memory is being used.

# For profiling C and C++ programs.
# For profiling a Python, there are a bunch of different tools that are disposal, depending on what exactly we want to
# profile.

# We can be as detailed as profiling the memory usage of a single function, or as big picture as monitoring
# the total memory consumption over time. Using profilers, we can see what structures are using the most memory at
# one in time or take snapshots at different points in time and compare them.

# The goal of these tools is to help us identify which information we're keeping in memory that we don't actually need.
# It's important that we measure the use of memory first before we try to change anything, otherwise we might be
# optimizing the wrong piece of code.

# Sometimes we need to keep data in memory, and that's fine, but you want to make sure that you're only keeping the data
# that you actually need, and that you've let go of anything you won't be using, that way the garbage collector can
# give that memory back to the OS. Of course, if you check that you're using the memory correctly,
# but still find that your exhausting available RAM, it might be time for an upgrade.

"""Managing Disk Space"""
# Another resource that might need our attention is the disk usage of our computer.

# Programs may need disk space for lots of different reasons:
# - installed binaries and libraries,
# - data stored by the applications,
# - cached information,
# - logs,
# - temporary files,
# - backups.

# If our computers running out of space, it's possible that we're trying to store too much data in too little space.
# Maybe we have too many applications installed, or we're trying to store too many large files in the drive.
# But it's also possible that programs are misusing the space allotted (given) to them, like by keeping temporary files
# or caching information that doesn't get cleaned up quickly enough or at all.

# It's common for the overall performance of the system to decrease as the available disk space gets smaller.
# Data starts getting fragmented across the disk, and operations become slower. When a hard drive is full, programs may
# suddenly crash, while trying to write something into disk and finding out that they can't. A full hard drive might
# even lead to data loss, as some programs might truncate a file before writing an updated version of it, and then fail
# to write the new content, losing all the data that was stored in it before.

# If it gets to this point, we'll probably see some error, like 'No space left on device' when running our applications
# or in the logs. So what do you do if a computer runs out of disk space?

# If it's a user machine, it might be easily fixed by uninstalling applications that aren't used, or cleaning up old
# data that isn't needed anymore.

# But if it's a server, you might need to look more closely at what's going on.
# Is the issue that you need to add an extra drive to the server to have more available space, or is it that some
# application is misbehaving and filling the disk with useless data?

# To figure this out, you want to look at how the space is being used and what directories are taking up the most space,
# then drill down until you find out whether large chunks of space are taken by valid information or by files that
# should be perched.

# For example, on a database server, it's expected that the bulk of the disc space is going to be used by the data
# stored in the database.
# A mail server, it's going to be the mailboxes of the users of that service.
# But if you find that most of the data is stored in logs or in temporary files, something has gone wrong.

# One common pattern of misbehavior is a program that keeps logging error messages to the system log over and over.
# This can happen for lots of different reasons. open logging error messages.png

# For example, the OS might keep trying to start a program that fails because of a configuration problem.
# This will generate a new log entry with every retry, and can take up a lot of space if there are several retries per
# second, or it could be that server has a lot of activity and the logs are real. But there are just too many of them.

# In that case, you might want to look on the tweaking the configuration of the tools that rotate the logs more
# frequently, to make sure that you're keeping only what you need.

# In other cases, the disk might get full due to a program generating large temporary files, and then failing to clean
# those up. For example, an application might clean up temporary files when shutting down cleanly, but leave them behind
# if it crashes. Or it could simply be a programming error of creating temporary files and never cleaning them up.
# In a case like this, you'll ideally have some housekeeping to fix the program, and delete those files correctly.
# But if that's not possible, you might need to write your own script that gets rid of them.

# A situation that might be tricky to debug is when the files taking up the space of deleted files.

# How can deleted files take up space? - If a program opens a file, the OS lets that program read and write in the file
# regardless of whether the file is marked as deleted or not. So lots of programs delete the temporary files they
# create right after opening to avoid issues with failing to clean them up later. That way, the process can read from
# and write to the file while the file is open. Then, when the process finishes, the file gets closed and actually
# deleted.

# This system is widely used and works fine for most processes. But if for some reason, this temporarily deleted file
# starts becoming super large, it can end up taking all the available disk space.
# If that happens, we'll be left scratching our heads when trying to figure out where most of the data went,
# since we won't see these deleted files.

# To check for the specific condition, we need to list the currently opened files, and comb for the ones that we know
# are deleted. open grep_deleted.png

# Of course, there are all kinds of other reasons why the disk may be getting too full.
# Just remember that whenever this happens, your process will remain the same. You'll need to spend some time looking
# into what's using the disk. Check to see if it's expected or an anomaly, figure out how to solve it,
# and most important of all, how to prevent it from happening again?
