"""Possible Causes of Slowness"""

# 1. When trying to figure out what's making a computer slow, the first step is to look into WHEN the computer is slow?
# If it's slow when starting up, it's probably a sign that there are too many applications configured to start on boot.
# Fix: just go through the list of programs that start automatically and disabling any that aren't really needed.

# 2. If the computer becomes sluggish after days of running just fine, and the problem goes away with a reboot, it
# means that there's a program that's keeping some state while running that's causing the computer to slow down.
# For example, this can happen if a program stores some data in memory and the data keeps growing over time, without
# deleting old values. If a program like this stays running for many days, the data might grow so much that reading it
# becomes slow and the computer runs out of RAM. This is almost certainly a bug in the program.
# And the ideal solution for a problem like this is to change the code so that it frees up some memory used.
# If you don't have access to the code, another option is to schedule a regular restart to mitigate both the slow
# program and your computer running out of RAM.

# 3. A similar problem that can trigger after a long time using an application, and that isn't solved by a reboot,
# is that the files that an application is handling have grown too large. So when the program needs to read those files,
# it gets really slow. Again, this generally points to a bug in the way the program was designed because it didn't
# expect the files to grow so large. The best solution in this case is to fix the bug.

# But what can you do if you can't modify the code of the program?

# Logrotate

# You can try to reduce the size of the files involved.
# If the file is a log file, you can use a program like 'Logrotate' to do this for you.
# For other formats, you might need to write your own tool to rotate the contents.

# Another data point that we can use to diagnose what's going on is WHEATHER this happens for ALL users of the
# application or just a subset of them.
# If only some users are affected, we'll want to know if there's something that's configured differently on those
# computers that might be triggering the slowness.
# For example, many operating systems include a feature that tracks the files in our computer, so it's easy and fast to
# search for them. This feature can be really useful when looking for something on a computer, but can get in the way
# of everyday use if we have tons of files and not the most powerful hardware.

# We've called out before that reading from the network is notably slower than reading from disk.
# It's common for computers in an office network to use a file system that's mounted over the network, so they can share
# files across computers. This normally works just fine, but can make some programs really slow if they're doing a lot
# of reads and writes on this network-mounted file system. To fix this, we'll need to make sure that the directory used
# by the program to read and write most of its data is a directory local to the computer.

# Hardware failures can also cause our computer to become slow.
# If your hard drive has errors, the computer might still be able to apply error correction to get the data that it
# needs, but it will affect the overall performance. And once a hard drive starts having errors, it's only a matter of
# time until they're bad enough that data starts getting lost, so it's worth keeping an eye out for them.

# To do this, we can use some OS utilities that diagnose problems on hard drives or on RAM, and check if there's
# anything that could be causing problems.

# 4. Yet another source of slowness is malicious software. Of course, we always want to keep our computer clean of any
# malicious software, but we can feel the effects of malicious software even if they aren't installed.
# For example, you might have come across a website that includes scripts, either in the website's content or the ads
# displayed, that use our processor to mine for cryptocurrency. Malicious browser extensions also fall into this
# category.

