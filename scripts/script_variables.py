import os
import subprocess
# maybe, this script runs correctly only on Linux
# Open screenshot C:\pythonProject\Automation with Python\screenshots\variables.png


# When we retrieve a value from
# a dictionary using the key as in
# OS.environ[fruit] and the key
# isn't present, we get an error.
# If we use a getMethod instead,
# we can specify what value should be
# returned if the key isn't present.
# In other words, the getMethod allows us to specify
# a default value when the key that
# we're looking for isn't in the dictionary. So what we're asking Python to do is
# try to retrieve the value associated with the key,
# but if the key's not
# defined return an empty string instead.

print("HOME: " + os.environ.get("HOME", ""))  # get the value of environment variables
print("SHELL: " + os.environ.get("SHELL", ""))
# print("FRUIT: ", + os.environ.get("FRUIT", ""))
print(f"FRUIT: {os.environ.get('FRUIT', '')}")

# We got the values for home and shell, but not for fruit.
# Well, that's because that
# variable isn't defined in the current environment.
# To define it in a way that
# our script we'll be able to see it,
# we need to run this in our command-line.
# So we define the variable by just setting
# a value using the equal sign
# and leaving no spaces in between.
# Along with this, the export keyword tells a shell that we
# want the value we set to be
# seen by any commands that we call.

result = subprocess.run("dir", shell=True)
print(result.returncode, result.stdout)
