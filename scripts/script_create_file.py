# open C:\pythonProject\Automation with Python\screenshots\create_file.png
import os
import sys


filename = sys.argv[0]  # in video sys.argv[1] but here it returns IndexError: list index out of range.
# That's because this script should be run from cmd with argument which is name of file, e.g. ./script_create_file.py new_file
# In this case script will run successfully as sys.argv[1] will be 'new_file' parameter
if not os.path.exists(filename):
    with open(filename, 'w') as file:
        file.write('New file created\n')
else:
    print(f'Error, the file {filename} already exists.')
    sys.exit()
