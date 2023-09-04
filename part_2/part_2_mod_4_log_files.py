"""Filtering Log Files with Regular Expressions"""

# open a file received as a parameter of our script - read C:\pythonProject\Automation with Python\scripts\script_check_log.py
# and open screenshot script_log.png, script_log_2.png
# Remember that for performance reasons, when files are large, it's generally a good practice to read them line by
# line instead of loading the entire contents into memory.

# We're using the same syslog (open script_myapp.py), and we want to display the date, time, and process id that's inside the square brackets.
# We can read each line of the syslog and pass the contents to the show_time_of_pid function. Fill in the gaps to
# extract the date, time, and process id from the passed line, and return this format: Jul 6 14:01:23 pid:29440.
import re

# my solution
# def show_time_of_pid(line):
#     pattern = r'([A-Z][a-z]+ [\d] [\d]+:[\d]+:[\d]+).*([\d]{5})'
#     result = re.search(pattern, line)
#     return f'{result[1]} pid:{result[2]}'


# ChatGPT solution
def show_time_of_pid(line):
    pattern = r'([A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}).*\[(\d+)]'
    result = re.search(pattern, line)
    if result:
        return f'{result.group(1)} pid:{result.group(2)}'
    else:
        return "No match found"


# print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440
# print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187
# print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187
# print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440
# print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807
# print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440
# print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440


"""Making Sense out of the Data"""
# dictionaries are great structure to use when we want to count appearances of strings.
# We'll store the username as a keys of a dictionary, and we'll use the value to count the number of times that each
# username appears in the file.
# To do this in fewer lines, we'll use the get() method.

# we're taking the current value in the dictionary by passing a default value of zero, so that when the key is
# in present in the dictionary, we had a default value. We then add one and set it as a new value associated with that
# key. We then add 1 and set it as a new value associated with that key.
usernames = {}
name = 'good_user'
usernames[name] = usernames.get(name, 0) + 1  # {'good_user': 1}
print(usernames)
usernames[name] = usernames.get(name, 0) + 1  # {'good_user': 2}
print(usernames)

# continue in script_check_log.py
