"""Finding the Root Cause"""
# Understanding the root cause is essential for performing the long-term remediation.
# So how do we go about finding the actual root cause of the problem?
# Follow a cycle:
# 1. looking at the information we have
# 2. coming up with a hypothesis that could explain the problem
# 3. testing our hypothesis.

# If we confirm our theory, we found the root cause. If not - go back to the beginning and try different possibility.

# Where find possibilities ideas:
# a) searching online for the error messages that we get
# b) looking at the documentation of the applications involved
# c) ask colleagues if they had similar problems

# Whenever possible, check hypothesis in a test environment, instead of production env that our users are working with.
# Even when it seems that the error might be related to the specific production environment, it's always a good idea to
# check if we can reproduce the problem in a test environment before we modify production. So we'd always start by
# setting up a test instance of the service and checking if the problem replicates there before touching the production
# instance.

"""Tools"""

# iotop
# iostat
# vmstat
# ionice
# iftop
# rsync -bwlimit
# nice


# So say we have a test server running the same websites. When we start the backup, we see that the website stop
# responding. This is great because we have re-production case, and we can debug it properly.

# How do we find the root cause?

# It could be too much disk input and output.
# Use 'iotop' - tool similar to 'top' that lets us see which processes are using the most input and output.

# Other related tools: 'iostat' and 'vmstat'. Show statistics on the input/output operations and the virtual memory
# operations.

# If the issue is that the process generates too much input or output, we could use a command like 'ionice' to make our
# backup system reduce its priority to access the disk and let the web services use it too.

# What if the input and output is not the issue?

# Another option would be that the service is using too much network because it's transmitting the data to be backed up
# to a central server and that transmission blocks everything else.

# We can check this using 'iftop', yet another tool similar to 'top' that shows the current traffic on the network
# interfaces.

# If the backup is eating all the network bandwidth, we could look at the documentation for the backup software and
# check if it already includes an option to limit the bandwidth.

# The 'rsync' command, which is often used for backing up data, includes a -bwlimit, just for this purpose.

# If that option isn't available, we can use a program like 'Trickle' to limit the bandwidth being used.

# But what if the network isn't the issue either?

# Another option could be that the compression algorithm selected is too aggressive, and compressing the backups is
# using all of the server's processing power. We could solve this by reducing the compression level or using
# 'nice' command to reduce the priority of the process and accessing the CPU.

# If that's still not the case, we need to keep looking, check logs to see if we find anything that we missed before.
# Maybe look online for other people dealing with similar problems related to interactions of the backing up
# software with the web surfing software, and keep doing this until we come up with something that could be causing our
# problem.

