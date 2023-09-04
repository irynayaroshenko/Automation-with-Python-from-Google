"""Debugging a Python Crash"""
# We have a script that updates the descriptions of some products in our company's database.
# It's a pretty simple script that takes a CSV file as a parameter, which includes the data that needs to be
# imported using the product code and description.
# Our script simply reads through a file and then updates the database.
# Most of the time it works just fine. But when the file with the new descriptions is generated by one specific user,
# the program fails with an exception. The user has sent us a file that's failing so that we can try to figure out
# what's going on.

# Let's first check out the contents of the file:

# cat new_products.csv

# Okay, this seems harmless enough. open debug_python_script_1.png

# Let's try executing the program:

# ./update_products.py new_products.csv

# open debug_python_script_2.png
# The program failed with an exception. At the bottom, we see the name of the exception: KeyError and the message
# 'product_code', which is the name of the key that's failing.

# Above that, we see a list of function calls with two lines per function.
# The first line tells us the Python file that contains the function, the line number, and the name of the function.
# The second line shows us the contents of that line. open debug_python_script_3.png
# This information is similar to the backtrace that we saw in our last video. But the order of the functions is reversed

# The function at the bottom, 'update_data', is the one where the exception occurred.
# Above it, we see that update_data() was called by main(), and on top of that we see that main() was called by the line
# at the module level. open debug_python_script_4.png

# So what's going on here?
# The update_data() function is trying to access the 'product_code' fields in a variable named 'row'.
# But for some reason this is failing with a KeyError. open debug_python_script_5.png

# Frequently, knowing the exception message and the line where the exception happened, is already enough to understand
# what's going on. But in some cases like this one, that's not enough.

# It's time to try our hand at using a Python debugger. We'll start the debugger by running 'pdb3' and then  passing
# script that we want to run and any parameters that our script needs:

# pdb3 update_products.py new_products.csv

# open debug_python_script_6.png
# When we start the debugger it gets positioned at the first line of our script and waits for us to tell it what to do.
# We could run each of the instructions in the file one by one using the 'next' command.
# But there's a lot going on here. So we need to go through a lot of lines until we reach the failure.

# Alternatively, we can tell the debugger to 'continue' the execution until it either finishes or crashes:

# continue

# open debug_python_script_7.png
# So the program failed in the same way we'd seen before. But now we can use the debugger to get a better idea of why
# we're getting this pesky KeyError. Let's print the contents of 'row':

# print(row)

# open debug_python_script_8.png
# That's really weird. What are those characters appearing before product code? open
# If we search online for the sequence of characters, we find that they represent the Byte Order Mark or BOM which is
# used in UTF-16 to tell the difference between a file stored using Little-endian and Big-endian.

# Our file is in UTF-8, so it doesn't need the BOM. But some programs still include it and this is tripping up our
# script. So what can we do?

# Fortunately, others have already faced the same issue and figured out a solution. There is a special value called
# 'utf-8-sig' that we can set as the encoding parameter of the open() function.
# Setting this encoding means that Python will get rid of the BOM when files include it and behave as usual when they
# don't.

# Let's change the code of our script to use that encoding instead of the default. We'll look for the place where it's
# opening the file, then add the encoding='utf-8-sig' as the value. open debug_python_script_9.png

# Check if it works:

# ./update_products.py new_products.csv

# open debug_python_script_10.png
# We've fixed the problem. Our script can now work with users generating files with and without the Byte Order Mark.

# 'Breakpoints' let code run until certain line of code is executed.
# 'Watchpoints' let code run until a variable or expression changes.

"""Resources for Debugging Crashes"""
# https://realpython.com/python-concurrency/
# https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32
# https://stackoverflow.com/questions/33047452/definitive-list-of-common-reasons-for-segmentation-faults
# https: // sites.google.com / a / case.edu / hpcc / hpc - cluster / software / programming - computing - languages / cc / debugging - segmentation - faults

# Readable Python code on GitHub:
# https://github.com/fogleman/Minecraft
# https://github.com/cherrypy/cherrypy
# https://github.com/pallets/flask
# https://github.com/tornadoweb/tornado
# https://github.com/gleitz/howdoi
# https://github.com/bottlepy/bottle/blob/master/bottle.py
# https://github.com/sqlalchemy/sqlalchemy
