"""Why is my computer slow?"""
# Each application gets a fraction of the CPU time, and then the next application gets a turn.
# If you run too many applications or if one of these applications needs more CPU time than the fraction it's getting,
# things might become frustratingly slow.
# The general strategy for addressing slowness is to identify the reason for addressing slowness in our device,
# our script, or our system to run slowly. The bottleneck could be the CPU time as we just mentioned.
# But it could also be time spent reading data from disk waiting for data transmitted over the network, moving data
# from disk to RAM, or some other resource that's limiting the overall performance.

# If we've closed everything that wasn't needed and the computer is still slow, we need to look into other possible
# explanations.
# What if the hardware we're using just isn't good enough for the applications we're trying to run on it?
# In cases like these, will have to upgrade the underlying hardware.
# But to make a difference in the resulting performance, we need to make sure that we're actually improving
# the bottleneck and not just wasting our money on new hardware that will go unused.

# We need to monitor the usage of our resources to know which of them is being exhausted (means that it's being used
# completely and programs are getting blocked by not having access to more of it).
# Is it the CPU, the memory, the disk IO, the network connection, the graphics card?

# To find out, we use the tools available in our operating system, monitor the usage of each resource, and then work
# out which one is blocking our programs for running faster.

# top   (for Linux open top_commnd_linux.png)


# 'top' shows which currently running processes are using the most CPU time.
# If we start by memory, which ones are using the most memory. Also shows a bunch of other load information related
# to the current state of the computer, like how many processes are running and how the CPU time or memory is being used

# iotop
# iftop

# show which processes are currently using the most disk IO usage or the most network bandwidth.

# On macOS, the OS ships with a tool called 'Activity Monitor' which lets us see what's using the most CPU,
# memory, energy, disk, or network.

# On Windows, there's a couple of OS tools called 'Resource Monitor' and 'Performance Monitor' which also let us analyze
# what's going on with the different resources on the computer including CPU, memory, disk and network.


"""How Computers Use Resources"""

# When thinking about making things faster, it's important to understand the different speeds of the parts involved.
# When an application is accessing some data, the time spent retrieving that data will depend on where it's located.

# 1) If it's a variable that's currently being used in a function, the data will be in the CPU's internal memory,
# and our program will retrieve it really fast.
# 2) If the data is related to running program but maybe not the currently executing function, it will likely be in RAM,
# and our program will still get to a pretty fast.
# 3) If the data is in file, our program will need to read it from disk, which is much slower than reading it from RAM,
# 4) Reading information from over the network, we have a lower transmission speed, and we also need to establish the
# connection to the other endpoint to make the transmission possible, which adds to total time needed to get to data.
# So if you have a process that requires repeatedly reading data over the network, you might want to figure out if you
# can read it once stored on disk, and then read it from disk afterwards.
# Or similarly, if you're repeatedly reading files from disk, you might see if you can put the same information
# directly into the process memory and avoid loading it from disk every time.

# In other words, you want to consider if you can create a 'cache' which stores data in a form that's faster to access
# than its original form.

# There's a ton of examples of caches in IT:
# 1) A web proxy is a form of cache. It stores websites, images, or videos that are accessed often by users behind the
# proxy. So they don't need to be downloaded from the Internet every time.

# 2) DNS services usually implement a local cache for the websites they resolve. So they don't need to query from the
# Internet every time someone asks for their IP address.

# 3) The operating system also takes care of some caching for us. It tries to keep as much information as possible in
# RAM so that we can access it fast. This includes the contents of files or libraries that are accessed often, even if
# they aren't in use right now. We say that these contents are cached in memory.
# We say that if the data is part of a program that's currently running, it will be in RAM.

# But RAM is limited.
# If you run enough programs at the same time, you'll fill it up and run out of space. What happens when you run out of
# RAM?
# At first, the OS will just remove from RAM anything that's cached, but not strictly necessary.
# If there's still not enough RAM after that, the operating system will put the parts of the memory that aren't
# currently in use onto the hard drive in a space called 'swap'.

# Reading and writing from disk is much slower than reading and writing from RAM. So when the swapped out memory is
# requested by an application, it will take a while to load it back. The swapping implementation varies across the
# different OS, but the concept is always the same: the information that's not needed right now is removed from RAM
# and put onto the disk, while the information that's needed now is put into RAM. This is normal operation, and most of
# the time, we don't notice it. But if the available memory is significantly less than what the running applications
# need, the OS will have to keep swapping out the data that's not in use right now to move the data currently in use to
# RAM, and as we called out, our computer can switch between applications very quickly, which means that the data
# currently in use can also change very quickly. The computer will start spending a lot of time writing to disc to make
# some space in RAM and then reading from disk to put other things in RAM. This can be super slow.

# So what do you do if you find that your machine is slow because it's spending a lot of time swapping?
# There are basically 3 possible reasons for this:

# 1) if there are too many open applications and some can be closed, close the ones that aren't needed.
# 2) if the available memory is just too small for the amount that computer is using, add more RAM to the computer.
# 3) one of the running programs may have a memory leak, causing it to take all the available memory.

# A memory leak means that memory which is no longer needed is not getting released.
# For now, let's just say that if a program is using a lot of memory and this stops when you restart the program,
# it's probably because of a memory leak
#



