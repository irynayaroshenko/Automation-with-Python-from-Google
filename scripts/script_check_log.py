import re
import sys


logfile = sys.argv[1]
usernames = {}

with open(logfile) as f:
    for line in f:
        if 'CRON' not in line:
            continue
        pattern = r'USER \((\w+)\)$'
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
        # print(result[1])
        # print(line.strip())
    print(usernames)

# run ./script_check_log.py syslog
# syslog should contain:
# Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)
# Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)
# Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)
# Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)
# Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"
# Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)
# Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)


# sys.argv attribute is a list in Python that contains the command-line arguments passed to the script when it is
# executed. The sys.argv[0] element represents the script's filename itself, while subsequent elements
# sys.argv[1], sys.argv[2], and so on, correspond to the additional arguments passed.

# In this case, sys.argv[1] is used to access the value of the first command-line argument passed to the script.
# The value is then assigned to the variable logfile, indicating that it is intended to represent the filename of a log file.

# For example, if you execute the script from the command line as follows: python script.py mylogfile.txt
# The value "mylogfile.txt" will be assigned to the logfile variable.

# This code snippet allows you to access the command-line arguments passed to the script and assign them to variables
# for further processing. In this case, it specifically retrieves the first argument and assigns it to the logfile variable.

# It's worth noting that the code assumes the presence of at least one command-line argument.
# If no arguments are provided when executing the script, accessing sys.argv[1] without proper error handling could
# raise an IndexError. It's recommended to include appropriate checks and handling to ensure the script can handle
# different scenarios gracefully.
