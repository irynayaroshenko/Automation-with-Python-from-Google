"""Unhandled Errors and Exceptions"""
# Correctly handling memory is a hard problem, and that's why there's a bunch of different programming languages like
# Python, Java, or Ruby that do it for us. But that doesn't mean programs written in these languages can't trigger weird
# problems. In these languages, when a program comes across an unexpected condition that isn't correctly handled in the
# code, it will trigger errors or exceptions.

# In Python, for example, we could get an IndexError if we tried to access an element after the end of a list.
# TypeError or AttributeError if we try to take an action on a variable that wasn't properly initialized or
# DivisionByZeroError if we tried to divide by zero.
# When the code generates one of these errors without handling it properly, the program will finish unexpectedly.
# In general, unhandled errors happen because the codes making wrong assumptions: maybe the program's trying to access
# a resource that's not present, or the code assumes that the user will enter a value but the user entered and empty
# string instead. Or maybe the application is trying to convert a value from one format to another and the value doesn't
# match the initial expectations.

# When these failures happen, the interpreter that's running the program will print the type of error, the line that
# caused the failure, and the traceback. The traceback shows the lines of the different functions that were being
# executed when the problem happened. In lots of cases, the error message and traceback info already gives us enough to
# understand what's going on, and we can move on to solving the problem. But sadly, that's not always the case.

# The fact that a piece of code crashes on one function doesn't mean that the error is necessarily in that function.
# It's possible, for example, that the problem was caused by a function called earlier which set variable to bad value.
# So the function where the code crashes is just accessing that variable.

# So when the error message isn't enough, we'll need to debug the code to find out where things are going wrong.
# For that, we can use the debugging tools available for the application's language.

# For a Python, program we can use the 'pdb' interactive debugger which lets us do all the typical debugging actions
# like executing lines of code one-by-one or looking at how the variables change values.
# (tried in Automation with Python/scripts/test.py)

# When we're trying to understand what's up with a misbehaving function on top of using debuggers, it's common practice
# to add statements that print data related to the code execution. Statements could show the contents of variables,
# the return values of functions or metadata like the length of a list or size of a file.
# This technique is called 'printf debugging'.

# The name comes from the 'printf' function used to print messages to the screen in the C programming language.
# But we can use this technique in all languages, no matter if we use 'print', 'puts', or 'echo' to display the text on
# the screen.

# When changing code to print messages to the screen, the best approach is to add the messages in a way that can be
# easily enabled or disabled depending on whether we want the debug info or not.

# In Python, we can do this using the 'logging' module.
# This module, lets us set how comprehensive we want our code to be. We can say whether we want to include all debug
# messages, or only INFO, WARNING or ERROR messages. Then when printing the message, we specify what type of message
# we're printing. That way, we can change the debug level with a flag or configuration setting.

# So you figured out why the unexpected exception was thrown, what do you do next?

# The solution might be fixing the programming error like making sure variables are initialized before they're used or
# that the code doesn't try to access elements after the end of a list. Or it could be that certain use cases that
# hadn't been considered needs to be added to the code. In general, you'll want to make the program more resilient to
# failures.

# Instead of crashing unexpectedly, you want the program to inform the user of the problem and tell them what they need
# to do.

# For example, say you have an application that crashes with a 'Permission denied' error.
# Rather than the program finishing unexpectedly, you'll want to modify the code to catch that error and tell
# the user what the permission problem is, so they can fix it.

# For example, unable to write new files in /temp/ dir, make sure your user has right permissions on temp directory.

# In some cases, it doesn't make sense for our program to even run if certain conditions aren't met.
# In that case, it's okay for the program to finish when the error is triggered. But again, it should do so in a way
# that tells the user what to do to fix the problem.

# For example, if it's critical for an application to connect to a database but the database server isn't responding,
# it makes sense for the application to finish with an error saying 'Unable to connect to the database server'.
# It also makes sense to include all details of the attempted connection like:
# - host name,
# - port,
# - username used to connect.

# So to recap, if your program is crashing with an 'Unhandled error', you want to first do some debugging to figure out
# what's causing the issue. Once you figured it out, you want to make sure that you fix any programming errors and that
# you catch any conditions that may trigger an error. This way, you can make sure the program doesn't crash and leave
# your users frustrated.

"""Fixing Someone Else's Code"""
# If someone else's code has comments and the functions are well-documented, reading these is a great place to
# start when trying to figure out what's going on. Writing good comments is one of those good habits that pays off when
# trying to understand code written by others and also your past self.

# Unfortunately, a lot of code doesn't include enough comments, leaving us to try to understand it without enough
# context. If that's the case, you can improve things by adding comments as you read the code and figure out what it's
# doing. Writing these comments help you solidify your understanding. If you contribute those comments back to the
# original developers, you can help anybody else trying to understand the code.

# Another thing that can help to understand someone else's code is reading the tests associated to the code.
# Well-written tests can tell us what each function is expected to do. Looking at the existing tests can show
# us which use cases weren't taken into account. But what if there aren't enough tests?

# Just like with writing extra comments, writing some tests of your own can help you better see what the code is
# supposed to do and improve overall quality of the code. This can also be really useful when modifying the original
# code. To ensure that changes you make, don't break the rest of the functionality.

# In the end, to really understand what's going on, you just have to read through the code.
# But how do you even start reading through someone else's code?

# This depends a bit on personal preference and the size of project. If there are only a couple of 100 lines of code,
# it's feasible to read all of them. But when the project has thousands or tens of thousands of lines of code,
# you can't really read the whole thing. You'll need to focus on the functions or modules that are part of
# the problem that you're trying to fix. One possible approach in this case, would be to start with the function
# where the error happened, then the function or functions that call it, and so on until you can grasp the contexts
# that led to the problem.

# While this is of course much easier if it's in a programming language that you're familiar with, you don't need to be
# an expert in the language to fix a bug in the program. If you've come across an error and debug the issue well enough
# to understand what's going on, you might be able to fix the problem even if you've never seen that language before.
# This is one of those skills that gets better with practice.
