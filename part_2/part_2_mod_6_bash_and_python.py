"""Choosing Between Bash and Python"""
# Need to be careful not to quickly make commands unreadable, e.g.,
# for i in $(cat story.txt); do
#   B=`echo -n "${i:0:1}" | "[:lower:]" "[:upper:]"`;
#   echo -n "${B}${i:1} ";
#   done;
#   echo -e "\n"

# open unreadable_bash_example.png
# This command line is using some stuff we saw and some that we didn't, like how to do indexing on bash strings to
# turn the first letter of each word into uppercase.
# This command line is pretty unreadable. If there happened to be a bug in it, it'd be hard to figure out how to fix it.
# When a bash command line starts becoming this complex,
# it's a better to write a Python script that handles data in a more readable way:
# open capitalize_words.py

# Once we have this script, we can execute it as part of a pipeline:
# cat story.txt | ./capitalize_words.py
# open unreadable_bash_example_fixed.png


# Conclusion
# Good idea to choose bash when we're operating with files and system commands,
# as long as what we're doing is simple enough that the script is self-explanatory.
# As soon as it becomes hard to understand what the script is doing, it's better to write it in a more general
# scripting language like Python.
# Bash scripts aren't as flexible or robust as having entire Python language available, with its many functions to
# Availability of Bash and Linux commands depends on the platform that we're using.
# Some commands might not be present on certain OS.
# Running a bash script can get the job done very quickly on a Linux machine, but it won't work on a Windows.
# There, we need to write the same script in PowerShell.
# So if the tasks that you're trying to accomplish is limited to the current server or a fleet of servers,
# all running the same OS, a simple bash script can get the job done.
# But if your code is complex, or it needs to work across platforms, you might be better off using the Python
# standard library or other external modules that provide the same functionality.
# Lastly, there are lots of situations where either a bash script or a Python script might solve the problem just fine.
# In those cases, you can choose whichever one you feel more comfortable with.

