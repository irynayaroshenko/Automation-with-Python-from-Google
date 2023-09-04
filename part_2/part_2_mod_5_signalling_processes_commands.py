"""Signalling Processes"""
# Using signals, we can tell a program that we want it to pause or terminate.
# We can also cause it to reload its configuration, or to close all open files.

# Example:
# ping www.example.com

# Ctrl-C
# The ping command is now running, sending ICMP packets to machine over the network once per second.
# And it will keep running forever unless we interrupt it (Ctrl-C). Open screenshot ping_command.png

# What's happening behind the scenes is the process received a signal indicating that we wanted it to stop.
# When that signal's received, the process does whatever it needs to finish cleanly.
# The signal that control see sense is called SIGINT.

# Ctrl-Z
# If interrupt ping with Ctrl-Z the process didn't finish properly. (Open screenshot ping_ctrl_z.png)
# We get a message saying that it's stopped. The signal that we sent is called SIGSTOP.
# This signal causes the program to stop running without actually terminating.
# But don't worry, we can make it run again by executing fg

# fg
# If execute 'fg' after program was stopped with Ctrl-Z, program continue running (open screenshot fg_command.png)
# To stop again, use Ctrl-C, Ctrl-Z or other signal

# kill
# By default, kill will send a signal called SIGTERM that tells the program to terminate.
# Since kill is a separate program, we need to run it on a separate terminal.
# And we also need to know the process identifier or PID of the process that we want to send the signal to.

# ps
# list the currently running processes.
# Depending on what options that we pass, it'll show different subsets of processes with different amounts of detail.
# e.g. ps ax - lists all the running processes in the current computer

# We'll run ping on one terminal, and then find its PID and kill it from a second terminal (open kill_command_1.png)
# run ping www.example.com in 1st terminal
# run ps ax | grep ping in 2nd terminal

# ps and grep commands found that the PID for the running ping command is 4619.
# Use this PID to send the signal that we want using 'kill':
# kill 4619
# ('Terminated' appeared in 1st terminal, open kill_command_2.png)

# grep
# keep lines that contain the name of the process that we're looking for

"""
Redirections, Pipes and Signals

Managing streams
These are the redirectors that we can use to take control of the streams of our programs

    command > file: redirects standard output, overwrites file

    command >> file: redirects standard output, appends to file

    command < file: redirects standard input from file

    command 2> file: redirects standard error to file

    command1 | command2: connects the output of command1 to the input of command2

Operating with processes
These are some commands that are useful to know in Linux when interacting with processes.

    ps: lists the processes executing in the current terminal for the current user

    ps ax: lists all processes currently executing for all users  

    ps e: shows the environment for the processes listed  

    kill <PID>: sends the SIGTERM signal to the process identified by PID

    fg: causes a job that was stopped or in the background to return to the foreground

    bg: causes a job that was stopped to go to the background

    jobs: lists the jobs currently running or stopped

    top: shows the processes currently using the most CPU time (press "q" to quit)  
"""