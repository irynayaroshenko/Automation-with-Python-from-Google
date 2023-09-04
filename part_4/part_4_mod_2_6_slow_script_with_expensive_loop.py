"""Slow Script with Expensive Loop"""
# Remember that meeting reminder script that was having trouble with the dates?
# The developers have kept working on it. Now, send personalized emails with the name of the person getting email and
# the greeting. Unfortunately it seems to have made the application pretty slow.

# How to make the program faster?

# First, we'll need to reproduce the problem and figure out what slow means in this case.
# One user told us that the problem is visible when the list of recipients is long. To avoid spamming our colleagues
# while we're testing this issue we'll send reminders to a bunch of test users that we've created in our mail server.

# You might remember that the application has two parts: shell script that pops up a window where we can enter the data
# of the reminder and a Python script that prepares the email and sends it.
# The part that's slow is the sending of the emails. So we won't interact with the pop-up at all.

# We'll just pass the parameters we need to the Python script. We'll measure the script speed using the 'time' command.
# First with just one test user and see how long it takes:

# time ./send_reminders.py "2020-01-13|Example|test1"


# When we call 'time' it runs the command that we pass to it and prints how long it took to execute it.
# It has 3 different values:
#
# Real – amount of actual time it took to execute the command/script (usually longer than user + sys, because the
# computer might be busy at the same time with other operations). That’s why it’s sometimes referred to as
# ‘wall-clock time’ because it’s how much time a clock hanging on the wall would measure no matter what the computer
# is doing
# user – time spent doing the operations in the user space
# sys – time spent doing system level operations

# It took our script 0.129 sec to send the email. That's not a lot, but we only send the message to one user.

# Let's try this again with our nine tests users.

# time ./send_reminders.py "2020-01-13|Example|test1,test2,test3,test4,test5,test6,test7,test8,test9"

# We see that it took 0.296 seconds to send the email this time (open send_reminders_slowness_1.png).
# That's still not a lot, but it does look like it's taking longer with a longer list of emails.

# How can we find out what's wrong with the code?
# We could always look at the code and see if we find any expensive operations that we can improve.
# But in this case we want to use a profiler to get some data about what's going on.
# There's a bunch of different profilers available for Python that work for different use cases.

# We'll use the one called 'pprofile3'.

# pprofile3 -f callgrind -o profile.out ./send_reminders.py "2020-01-13|Example|test1,test2,test3,test4,test5,test6,test7,test8,test9"


# '-f' flag to tell it to use the 'callgrind' file format
# -o flag to tell it to store the output in the profile.out file

# This generated a file that we can open with any tool that supports the 'callgrind' format.

# We're going to use 'kcachegrind' to look at the contents, which is a graphical interface for looking into these files.

# kcachegrind profile.out       (open send_reminders_slowness_2.png)

# Open send_reminders_slowness_3.png. In the lower right half we see a call graph, which tells us that main() function
# is calling the send_message() function one time. This function is calling the message template function,
# the get_name() function, and the send message function 9 times each.
# The graph also tells us how many microseconds are spent on each of these calls.

# We can see that most of the time is being spent in the get_name() function.
# That's probably the one we should optimize.

# Let's see what this function is doing using atom. Open send_reminders_slowness_4_original_code.png
# So we see that the get_name() function opens a CSV file then goes through the whole file checking if the first field
# in the line matches the e-mail name and when that's the case it sets the value of the name variable.

# Couple of things that are wrong with this function:
# - once it finds the element in the list it should immediately break out of the loop.
# Right now, it's iterating through the whole file even if the email was found in the first line.
# - but even if we fixed that it would still open the file and read through it for each e-mail address.
# This can get really slow if the file has a lot of lines.

# How can we make this better?

# We can read the file once and store the values that we care about in a dictionary and then use that dictionary for the
# lookups.
# We'll change get_name() and turn it into a read_names() which will process the CSV file and store the values we want
# in the 'names' dict. For each line we store the 'email' as the key and the 'names' as the values. Instead of returning
# one name we'll return the whole dictionary.

# All right we have read_names() that stores the data we want in a dictionary. Open
# We now need to change the way this is called in the send_message()
# We see that the get_name() is being called once per email. To apply our change we should call the read_names() before
# for loop so that we do it only once. Then instead of calling get_name() we'll just get the values form the dictionary.
# open send_reminders_slowness_5_edit_code_2.png

# Let's save our file and profile our script again to see if we manage to make it any faster.

# pprofile3 -f callgrind -o profile.out ./send_reminders.py "2020-01-13|Example|test1,test2,test3,test4,test5,test6,test7,test8,test9"
# kcachegrind profile.out


# Open send_reminders_slowness_6.png.
# The graph looks different now as we've changed how the code behaves.
# See how the read_names() is now taking a much smaller portion of time. On the flip side we see that message_template()
# is the one that's taking the most time now. So if we wanted to keep making our script faster that's what we look next.
