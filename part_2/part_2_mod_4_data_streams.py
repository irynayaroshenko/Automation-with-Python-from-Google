"""I/O streams are the basic mechanism for performing input and output operations in your programs.
A shell is a command line interface used to interact with your operating system.
Python programs get executed inside a shell command-line environment.
The variable set in that environment which are called you guessed it environment variables are another source of
information that we can use in our scripts. Understanding and being able to change environment variables
can be really useful to quickly alter a program's behavior.
Usually, we can do this by just making some minor changes in the environment the programs are running in.
From a command line prompt, we can check these variables using the 'env' or 'nth' command."""

# echo is a command that we use to print texts and Linux shell.
# When we want to access the value of the variable in the shell, we need a prefix and name of the variable with
# a dollar sign. E.g. echo $PATH

# Command-Line Arguments and Exit Status (or Return Code)
# cmd-arguments are parameters that are passed to a program when it started.
import sys
# The list of arguments are stored in the sys module

print(sys.argv)  # ['C:\\pythonProject\\Automation with Python\\part_2_mod_4_data_streams.py']

# Exit status is a value returned by a program to the shell. In all Unix-like operating systems,
# the exit status of the process is zero when the process succeeds and different than zero if it fails.

# wc variables.py   (response: values of lines, words and characters for our Python script, e.g. 7 19 174 variables.py)
# echo $?   (response: 0)
# So here we first ran the WC command then we printed the contents dollar sign question mark variable, and we can see
# that the exit value was zero. That's because WC ran successfully.

# When a Python script finishes successfully, it exits with an exit value of zero.
# When it finishes with an error like type error or value error, it exits with a different value than zero.
# We can make it exit with whatever value is relevant.

"""Subprocesses"""
# Up to now, we've been using Python to interact with the operating system through baked in functionality.
# For example, we've used file objects to read the contents of files.Use the shutil module to check if the disk is full.
# And use a sys module to process standard input, get parameters, or generate an exit code.
# But what if we needed to run a system program from a Python script?
# Say, e.g., that as part of a Python script, we needed to send ICMP packets to a host to check if it's responding.
# We could try to look for an external module that provides this functionality.
# Or we can just run the 'ping' command, which will send packets for us. Sometimes it's easier or faster to use
# a system command as part of our Python script to accomplish a task, or use some functionality that doesn't exist
# in the Python modules, neither built in nor external.
# For these cases, Python provides a way to execute system commands in our scripts, using functions provided by
# the subprocess module.
# Let's check out an example.
# First, we'll import a subprocess module, and then we'll call the date command, which shows the current date using
# the 'subprocess.run' function.
import subprocess
import shutil

# print(subprocess.run(["date"]))  # works for Linux

# I couldn't find how to run this via subprocess.run on Windows. Below 2 solutions don't work.
# solution 1
# result = subprocess.run(["wmic", "path", "win32_operatingsystem", "get", "localdatetime"], capture_output=True, text=True)
# output = result.stdout.strip().split("\n")[1].strip()
# print(output)
# solution 2
# result = subprocess.run(["wmic", "path", "win32_operatingsystem", "get", "localdatetime"], capture_output=True, text=True, encoding="utf-8")
# output = result.stdout.strip().split("\n")[1].strip()
# print(output)

# This one works, but it doesn't use subprocess
# import datetime
# import win32timezone
#
# current_date = datetime.datetime.now(tz=win32timezone.TimeZoneInfo.local())
# output = current_date.strftime("%Y-%m-%d")
# print(output)

# !!! shell=True - important for Windows
result = subprocess.run(["echo", "Hello World"], shell=True, text=True)  # "Hello World"
result1 = subprocess.run("dir", shell=True)
print(result.returncode, result.stdout)  # 0 None


def command_path(command: str):
    cmd_path = shutil.which(command)
    if cmd_path is not None:
        return f'Absolute path for command "{command}" is: {cmd_path}'
    else:
        return f'Command "{command}" not found.'


cmd = 'rm'
print(command_path(cmd))

result = subprocess.run(["C:\Windows\system32\ping.EXE", "coursera.org"], capture_output=True, text=True)
print(result.stderr)  # (error output)
print(result.stdout)  # Pinging coursera.org [13.32.110.31] with 32 bytes of data:...  (normal output)
print(result.stdout.strip().split('\n'))  # ['Pinging coursera.org [13.32.110.31] with 32 bytes of data:', 'Reply from 13.32.110.31:...
print(result.returncode)  # 0 (checks exit value)

# result = subprocess.run(["C:\Windows\system32\ping.EXE", "google.coms"], capture_output=True, text=True)
# print(result.stderr)
# # print(result.stdout)
# print(result.stdout.strip().split('\n')) # ['Ping request could not find host google.coms. Please check the name and try again.']
# print(result.returncode)  # 1


# Give output to screen can be handy for system commands that either don't have useful output (like 'cp',
# 'chmod', 'sleep', and many others), or when we don't care about processing the output any further.
# In other words, when it's just fine to have the output, print it to the screen.

"""Obtaining the Output of a System Command"""
# put parameter capture_output=True in subprocess.run()
# If we want 'stdout' to become a proper string, we can call the 'decode' method. (Doesn't exist here)
# This method applies an encoding (UTF-8 by default) to transform the bytes into a string.
# print(result.stdout.decode)

"""Advanced Subprocess Management"""
# One way of providing information to our processes is to modify the environment variables.
# Using this mechanism, we can change where the process looks for executable files, which commands it uses
# interact with some parts of the system,the kind of output it'll generate and more.

# The usual strategy for modifying the environment of a child process is to first copy the environment seen by our process,
# do any necessary changes, and then pass that as the environment that the child process will see.
# open C:\pythonProject\Automation with Python\scripts\script_myapp.py

# With subprocess.run() we can use the 'cwd' parameter to change the current working directory where the command will be executed.
# This can be really helpful when working with a set of directories where you need to run a command on each of them.
#
# We could also set the 'timeout parameter'.
# This will cause the run function to kill the process if it takes longer than a given number of seconds to finish.
# This might be useful if you're running a command that you know might get stuck.
# For example, if it's trying to connect to a network and your computer is offline.
#
# Or we can also set the 'shell parameter'.
# If we set this to True, Python will first execute an instance of the default system shell and then run the given
# command inside it.
# This means our command line could include variable expansions and other shell operations.
# Without the shell parameter, this would not be possible.
