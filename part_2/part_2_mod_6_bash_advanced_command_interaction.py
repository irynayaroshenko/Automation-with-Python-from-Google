"""Advanced Command Interaction"""
# system log file locates in var/log/syslog and contains a trove of information about what's going on in the system.
# Important to learn how to get information out of it.

# tail var/log/syslog - last 10 lines from the file
# open syslog_tail.png

# First, log lines include the date and time of when the entry was added to the file,
# then the name of the computer, then the name and PID of the process that trigger the event and finally,
# the actual event that's being logged.

# Task.
# Say that we had a computer that was under significant load, but we didn't know why, and to find out we wanted to check
# what events are being logged the most to syslog.
# To do that we need to extract the part of the line that has the actual event without the date and time.
# We can use a command 'cut' which let us take only bits of each line using a field delimiter.
# In this example, we can split the line using spaces:

# tail var/log/syslog | cut -d' ' -f5-
# open syslog_tail_cut.png

# cut -d' ' - use a space as a delimiter, -f5- - print the field number 5 and everything that comes after it.

# pipe this to find out the lines that are repeated the most:
# cut -d' ' -f5- var/log/syslog | sort | uniq -c | sort -nr | head
# open most_repeated_lines_result.png

# Better to put this into a bash script where to process all files in var/log that end in log.
# Print the name of the file that we're processing and then use the same group of commands as before to
# print the top 5 lines in each file.
# open toploglines.sh

