"""Bash Scripting"""
# Imagine that you wanted to convert all image files in one directory from PNG to JPEG format.
# There's a command called 'convert' that you can use to do this.
# You could definitely do this in Python, by going through all the files in the directory using
# 'os.listdir' and can convert using 'subprocess.run'.
# But it would end up being a really complex script for something that's actually super simple.
# Well, you can do this in Bash with just three lines of code, making it more readable and a lot easier to maintain.

"""Basic Linux Commands"""
# Managing files and directories
#
#     cd <directory>: changes the current working directory to the specified one
#
#     pwd: prints the current working directory
#
#     ls: lists the contents of the current directory
#
#     ls <directory>: lists the contents of the received directory
#
#     ls -l: lists the additional information for the contents of the directory.
#     Result example:
#     -rw-r--r-- 1 user user 192 Jan 8 14:41 myfile.txt
#
#     '-rw-r--r--' indicates the permissions of the file.
#     '1' is the number of 'i' nodes that point to the file.
#     'user' 'user' (3rd and 4th columns) indicate the owner and the group to which the file belongs.
#     '192' is file size
#     'Jan 8 14:41' is date of last modification
#     'myfile.txt' is file name
#
#     ls -a: lists all files, including those hidden
#
#     ls -la: applies both the -l and the -a flags
#
#     mkdir <directory>: creates the directory with the received name
#
#     rmdir <directory>: deletes the directory with the received name (if empty)
#
#     rm <filename> / rm *: delete file with given name / delete all files in current dir
#
#     cp <old_name> <new_name>: copies old_name into new_name (cp ../spider.txt . - copy spider.txt from parent (previous)
#     dir to current dir; cp spider.txt otherfile.txt - create cope of spider.txt but with name otherfile.txt)
#
#     mv <old_name> <new_name>: rename or move old_name into new_name (mv myfile.txt new.txt - rename myfile.txt to new
#
#     touch <file_name>: creates an empty file or updates the modified file if it exists
#
#     chmod <modifiers files>: changes the permissions for the files according to the provided modifiers;
#     we've seen +x to make the file executable
#
#     chown <user> <files>: changes the owner of the files to the given user
#
#     chgrp <group> <files>: changes the group of the files to the given group
#
# Operating with the content of files
#
#     cat <file>: shows the content of the file through standard output
#
#     wc <file>: counts the amount of characters, words, and lines in the given file;
#     can also count the same values of whatever it receives via stdin
#
#     file <file>: prints the type of the given file, as recognized by the operating system
#
#     head <file>: shows the first 10 lines of the given file
#
#     tail <file>: shows the last 10 lines of the given file
#
#     less <file>: scrolls through the contents of the given file (press "q" to quit)
#
#     sort <file>: sorts the lines of the file alphabetically
#
#     cut -d <separator> -f <fields> <file>: for each line in the given file, splits the line according to the given
#     separator and prints the given fields (starting from 1) https://linuxize.com/post/linux-cut-command/
#
# Additional commands
#
#     echo "message": prints the message to standard output
#
#     date: prints the current date
#
#     who: prints the list of users currently logged into the computer
#
#     man <command>: shows the manual page of the given command;
#     manual pages contain a lot of information explaining how to use each command (press "q" to quit)
#
#     uptime: shows how long the computer has been running
#
#     free: shows the amount of unused memory on the current system
