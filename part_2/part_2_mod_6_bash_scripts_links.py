# open gether_information.sh
# script is calling 3 main commands: 'uptime', 'free', 'who', which lists users currently logged into the computer.
# It uses 'echo' command to print some other information and to make the output a bit more readable by leaving
#  empty lines between the commands.
# We're also calling the 'date' command to print the current date.
# To call this command, we're using a special notation by putting the command inside dollar sign parentheses.
# This indicates that the output of the command should be passed to the echo command and be printed to the screen.
# result: open gether_information_script_result.png

# Script is written with one command per line. That's a common practice, but it's not the only way.
# We could also write the commands on the same line using semicolons to separate them. Like this:

# echo "Starting at: $(date)"; echo
#
# echo "UPTIME"; uptime; echo
#
# echo "FREE"; free; echo
#
# echo "WHO"; who; echo
#
# echo "Finish at: $(date)"

# open gether_information_script_edit.png

"""Using Variables and Globs"""
# We can assign and define variables. To access the value of a variable in bash, we need to prefix the name of
# the variable with the dollar sign ($):
# example=hello
# echo $example

# There can be no spaces between the name of the variable and the equal sign, or between the equal sign and the value.

# Remember: any variable that you define in your script or in the command line is local to the environment where you
# define it. If you want commands from that environment to also see the variable, you need to export them using
# the 'export' keyword.

# Let's now modify script gether_information.sh: add a variable to it.
# We'll use it to make our script look nicer by adding lines in between each of the commands.
# Define a variable called 'line', and put a bunch of dashes in it.
# Instead of leaving empty lines, we'll print this variable to separate our commands.
# See iteration 2 in gether_information.sh

# Globs
# Globs are characters that allow us to create list of files.
# * and ? are the most common globs. Using these globs lets us create sequences of filenames that we can use as
# parameters to the commands we call an R scripts.

# In bash, using * in the command line we'll match all filenames that follow the format that we specify, e.g.,
# echo *.py return all .py files in current dir.

# If put * at the end of an expression we get the list of all files that start with a certain prefix.
# echo c*  (we get capitalize.py, check_lock.sh, etc.)

# echo *   (all files in current dir)

# ?
# used to match exactly one character. We can get the Python files with five characters in their name
# by using the five question marks together:
# echo ?????.py   (areas.py hello.py myapp.py)

# If you want to use this functionality in Python, it's available through the 'glob' module.

"""Conditional Execution in Bash"""
# In Python, we use the 'if' block and the condition is an expression that has to evaluate to true or false.
# In bash scripting, the condition use is based on the exit status of commands.

# We use $? to check command exit status
# In bash scripting an exit value of 0 means success.
# This logic is used by the if operator in bash. To create a conditional expression, we're going to call
# a command and if the exit status of that command is 0, then the condition will be considered True.

# Say we wanted to verify that the /etc/hosts file contains an entry for 127.0.0.1, which it should.
# Knowing that 'grep' will return it exit status of 0 when it finds at least 1 match and different than 0 if it doesn't,
# we can use it to do this verification.
# open check_localhost.sh
# open check_localhost_script_result.png

# test
# There is plenty of other conditions that we might want to check in our scripts: if the file exists, if two strings
# are equal, if a number is less than another number, and so on.
# To help us with evaluating these conditions, there is a command called 'test'.
# It evaluates the conditions received, and exits with 0 when they are true and with 1 when they're false.

# Example:
# if test -n "$PATH"; then echo "Your path is not empty"; fi
# open test_command_result.png
# -n checks if a string variable is empty or not

# Other example of the same command:
# if [ -n "$PATH" ]; then echo "Your path is not empty"; fi

# In this case, the command we're calling is the opening square bracket.
# This is an alias to the 'test' command, but to call it successfully, we also need to include a closing square bracket.
# When using this syntax, remember, that there needs to be a space before the closing bracket.


"""Bash Scripting Resources"""
# https://ryanstutorials.net/bash-scripting-tutorial/
# https://linuxconfig.org/bash-scripting-tutorial-for-beginners
# https://www.shellscript.sh
