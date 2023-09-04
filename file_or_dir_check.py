import os


directory = r'C:\pythonProject\Automation with Python'
for name in os.listdir(directory):
    fullname = os.path.join(directory, name)
    if os.path.isdir(fullname):
        print(f'{fullname} is a directory.')
    else:
        print(f'{fullname} is a file.')