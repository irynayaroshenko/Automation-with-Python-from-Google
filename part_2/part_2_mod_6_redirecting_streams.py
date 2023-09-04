"""Redirecting Streams"""
# Redirection is provided by the OS and can be really useful when you want to store the output of a command in a file,
# instead of just looking at it on a screen.
# To redirect the standard output of a program to a file use '>' or '>>" symbol.

# ./example.py > new_file.txt
# output of example.py will be written to new_file.txt (will be created if not exist or !overwritten! if exists)

# ./example.py >> new_file.txt
# output of example.py will be written to new_file.txt (will be !appended! to file)

# In a similar way we can also redirect standard input.
# Instead of using the keyboard to send data into a program, we can use '<' symbol to read the contents of a file.

# ./streams_err.py < new.file.txt

# Open screenshot redirect_standard_input.png
# we don't see the input on the screen in the STDIN portion (as input was read from a file).
# So it only appears in the STDOUT portion where we see that it read one of the two lines.
# This is also expected because the input function only reads until it encounters a new line character.

# Can be useful to redirect STD_err or to capture errors and diagnostic messages from a program. Use '2>' symbol:

# ./streams_err.py < new_file.txt 2> error_file.txt
#  Open screenshot redirect_std_err.png

# 2 in '2>' represents the file descriptor of the STDErr stream.
# In this context you can think of a file descriptor as a kind of variable pointing to an IO resource.
# In this case the STD Err stream.
# 0 and 1 are the file descriptors for STDIN and STDOUT.

# Redirection works with many other commands, e.g., echo (create a file using the 'echo' and redirect its output
# to the file that we want to create.)

# echo "Some content of file" > my_file.txt

# cat my_file.txt
# Some content of file
