import datetime
import os

# os.remove('novel.txt')  # delete file (if file doesn't exist, returns FileNotFoundError)
# os.rename('first_draft.txt', 'final_version.txt')  # rename file (if file doesn't exist, returns FileNotFoundError)

# os.path submodule can be used to check if file exists
print(os.path.exists('hello.py'))  # True
print(os.path.exists('some_new_file.txt'))  # False

# get file size in bytes
print(os.path.getsize('health_checks.py'))

# to check when the file was last modified. getmtime(filename) returns timestamp, e.g. 1687433332.7721539 here it's
# Unix Timestamp (it represents the number of seconds from January, 1st, 1970)
"""This was adopted years ago to store the times associated to files in computers.
Since that's when they started publishing Unix operating systems, Unix uses that date because there couldn't be any file
created before that time. While Unix timestamps have a 50-year history, they're still very much present today.
They're used by file systems to show when a file was created, accessed, or modified.
They are also used in other systems like databases."""
print(os.path.getmtime('scripts/script_disc_usage.py'))

# to make it human-readable we use datetime module
timestamp = os.path.getmtime('scripts/script_disc_usage.py')
dt_timestamp = datetime.datetime.fromtimestamp(timestamp)
print(dt_timestamp)

# file = "file.dat"
file = "scripts/script_disc_usage.py"
if os.path.isfile(file):
    print(os.path.isfile(file))  # returns if file exists
    print(os.path.getsize(file))  # returns file size
else:
    print(os.path.isfile(file))
    print("File not found")

# get absolute file path
print(os.path.abspath('part_2_mod_2_work_with_files_dirs.py'))  # C:\pythonProject\Automation with Python\part_2_mod_2_work_with_files_dirs.py

# get current working directory
print(os.getcwd())

# create new dir os.mkdir(), change current working directory os.chdir()
# os.mkdir('new_dir_test')
# os.chdir('new_dir_test')
# print(os.getcwd())
# os.chdir(r'C:\pythonProject\Automation with Python')
# print(os.getcwd())

# remove dir rmdir() - only empty dir. Get dir content with
# os.rmdir('new_dir_test')
# os.mkdir('testtest')
print(os.listdir(r'C:\pythonProject\Automation with Python'))

# Returns True of False when check if file is dir or a file
print(os.path.isdir('testtest'))
print(os.path.isfile('part_2_mod_1.py'))

# observe C:\pythonProject\Automation with Python\file_or_dir_check.py to see how os.path.join(directory, name) works
# By using the os.path.join function instead of explicitly adding a slash, we can make sure that our scripts work
# with all operating systems.

