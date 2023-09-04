"""It Doesn't Work"""
# There are some common questions that we can ask a user that simply report something doesn't work.
# 1) What were you trying to do?
# 2) What steps did you follow?
# 3) What was the expected result?
# 4) What was the actual result?

# If the ticketing system your company uses allows this, it's a good idea to include these questions in the form that
# users have to fill out when reporting an issue.
# This way we save time and can start asking more specific questions right away.

# !! When debugging a problem, we want to consider the simplest explanations first and avoid jumping into complex or
# time-consuming solutions unless we really have to.
# (That's why when a device doesn't turn on, we first check if it's correctly plugged in and that there's electricity
# coming from the plug before taking it apart or replacing it with a new device.)

# To figure out the root cause: apply a process of elimination, starting with the simplest explanations first and
# testing those until you can isolate the root cause.
# For example, you check if you can reproduce the issue on your own computer. - Yes.
# Check if other websites load normally, internet works. - Yes.
# Check if other internal services/websites work. - Some work, others - don't.
# You find out that service which doesn't load and service which was reported by user - both are hosted on the same
# server.
# Next, check that server.

# The server running the websites is a Linux machine, so you'll connect to it using SSH.
# You run the 'top' command which shows the state of the computer and processes using the most CPU and see that the
# computer is super overloaded.

# The load average in the first line says 40.
# The load average on Linux shows how much time a processor is busy in a given minute, with one meaning it was busy for
# the whole minute.
# So normally this number shouldn't be above the amount of processors in the computer.
# A number higher than the amount of processors means the computer is overloaded.

# You know this computer has 4 cores, so 40 is a really high number. You also see that most of the CPU time is spent
# in waiting. This means that processes are stuck waiting for the operating system to return from system calls.
# This usually happens when processes get stuck gathering data from the hard drive or the network.

# By looking at the list of processes, you realize that the backup system is currently running on the server,
# and it seems to be using a lot of processing time.

# Backing up the data on the system is super important. But currently, the whole system is unusable.
# So you decide to stop the backup system by calling 'kill-STOP'.
# This will suspend the execution of the program until you let it continue or decide to terminate it.

# After doing this, you're on 'top' once gain, and you see that the load is going down, and so processes are no longer
# stuck waiting for I/O. Then you try logging into the website, and this time the landing page loads.

# Also important when in a day other user says some other service doesn't work - not to tell him that you know what the
# problem is and will fix in a moment. Because it can be totally different issue. That's why it's important always ask
# those 4 questions from the top of file.

# This solution is immediate remediation.

"""Creating a Reproduction Case"""
# Simple reproduction case is when you can reproduce on your computer and with couple os steps (run the app, for example
# Complex reproduction case, e.g., app won't start on user's computer but works on your PC.

# So you suspect that the problem has to do with something in the user's environment or configuration. There could be
# a bunch of reasons why this could happen.
# It could be problems with the network routing, old config files interfering with a new version of the program,
# a permissions problem blocking the user from accessing some required resource, or even some faulty piece of hardware
# acting out.

# What to do?

# 1. Logs
# Which logs to read, will depend on the OS and the application that you're trying to debug.
# On Linux, you'd read system logs like /var/log/syslog and user-specific logs like '.xsession-errors' file located in
# the user's home directory.
# On macOS, on top of the system logs, you'd go through the logs stored in the '/Library/Logs' directory.
# On Windows, you'd use the 'Event Viewer' tool to go through the event logs.
# Lots of times, you'll find an error message that will help you understand what's going on, e.g,
# 'Unable to reach server', 'Invalid file format', or 'Permission denied'.

# If logs didn't help (no error message or the error message is super unhelpful like 'Internal system error').

# 2. Isolate the conditions that trigger the issue
# a) Do other users in the same office also experienced the problem?
# b) Does the same thing happen if the same user logs into a different computer?
# c) Does the problem happen if the applications config directory is moved away?

# Let's say that it's the config directory file. You ask the user to move it away without deleting it, and now the
# application starts correctly. So you ask the user to send you the contents of that directory. You copy them onto your
# computer, and the program fails to start. Bingo, you got your reproduction case.
# It's starting the program with that config in place.

# Having a clear reproduction case, let's do investigate the issue, and quickly see what changes it:
# a) Does the problem go away if you revert the application to the previous version?
# b) Are there any differences in the 'strace' log, or the 'ltrace' logs when running the application with the bug
# config and without it?

# Having a clear reproduction case, - share with others when asking for help (as long as you aren't sharing any
# confidential information of course).
# Options:
# a) use it to report a bug to the applications developers,
# b) ask for help from a colleague,
# c) ask for help from an Internet forum about the application if it's publicly available.

# So when trying to create a reproduction case, we want to find the actions that reproduce the issue, and we want these
# to be as simple as possible.
# The smaller the change in the environment and the shorter the list of steps to follow, the better.

# Once you have a reproduction case, you're ready to move on to the next step: finding the root cause.



