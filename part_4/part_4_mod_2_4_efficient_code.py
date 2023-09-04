"""Writing Efficient Code"""
# We should always start by writing clear code that does what it should and only try to make it faster if we realize
# that it's not fast enough.

# It's pretty hard to know in advance how fast your script will be and how long it will take you to make it faster.
# But as a rule, we aim first to write code that's readable, easy to maintain and easy to understand, because that lets
# us write code with fewer bugs. If there's something that's super slow, then yes, it makes sense to fix it,
# particularly if the script will be executed frequently enough that making it faster will save you more time than the
# time you spend optimizing it.
# But remember, trying to optimize every second out of a script is probably not worth your time.

# Keep in mind that we can't really make our computer go faster. If we want our code to finish faster, we need to make
# our computer do less work, and to do this, we'll have to avoid doing work that isn't really needed.

# There's a bunch of different things to do.
# The most common ones include:
# 1) storing data that was already calculated to avoid calculating it again;
# 2) using the right data structures for the problem
# 3) reorganizing the code so that the computer can stay busy while waiting for information from slow sources like disk
# or over the network.

# To know what sources of slowness we need to address, we have to figure out where our code is spending most of its time
# There's a bunch of tools that can help us with that called Profilers.
# 'profiler' is a tool that measures the resources that our code is using, giving us a better understanding of what's
# going on. In particular, they help us see how the memory is allocated and how the time spent.

# Because of how profilers work, hey are specific to each programming language.
# So we would use 'gprof' to analyze a C program but use the 'cProfile' module to analyze a Python program.

# Using tools like these, we can see which functions are called by our program, how many times each function was called
# and how much time are programs spent on each of them. This way we can find for example, that our program is calling
# a function more times than we originally intended or that a function that we thought would be fast is actually slow.

# To fix our code, we'll probably need to restructure it to avoid repeating expensive actions.
# In this context, expensive actions are those that take a long time to complete. Expensive operations include parsing
# a file, reading data over the network or iterating through a whole list.

"""Using the Right Data Structures"""
# Lists are sequences of elements.
# We can add, remove, or modify the elements in them. We can iterate through the whole list to operate on each of the
# elements.

# Different programming languages call them differently: ArrayList in Java, Vector in C++, Array in Ruby, Slice in Go.

# All these names refer to the same data structure that's fast to add or remove elements at the end.
# But adding or removing elements in the middle can be slow because all the elements that follow need to be repositioned
# It's fast to access the element in a specific position in the list, but finding an element in an unknown position
# requires going through the whole list. This can be super slow if the list is long.

# Dictionary store key value pairs.
# We add data by associating a value to a key. Then, we retrieve a value by looking up a specific key.
# Called HashMap in Java, Unordered Map in C++,  Hash in Ruby, and Map in Go.

# The map part in those names comes from how we're creating a mapping between a key and a value.
# The Hash part comes from the fact that to make the structure efficient, a hashing function is used internally to
# decide how the elements will be stored.
# The main characteristic of this structure is that it's superfast for looking up keys. Once we have our data stored in
# a dictionary, we can find the value associated to a key in just one operation.
# If it were stored in a list, we need to iterate through the list.

# So as a rule of thumb, if you need to access elements by position or will always iterate through all the elements,
# use a list to store them.
# This could be a list of all computers in the network, of all employees in the company, or of all products currently
# on sale for example.

# On the flip side, if we need to look up the elements using a key, we'll use a dictionary.
# This could be the data associated to a user which we'd look up using their username, the IP associated to a computer
# using the host name, or the data associated to a product using the internal product code.
# Whenever we need to do a bunch of these lookup operations, creating a dictionary and using it to get the data will
# take a lot less time than iterating over a list to find what we're looking for.

# But it doesn't make sense to create a dictionary and fill it with data if we're only going to look up one value in it.
# In that case, we're wasting time creating the structure when we could just iterate over the list and get the element
# we're looking for.

# Another thing that we might want to think twice about is creating copies of the structures that we have in memory.
# If these structures are big, it can be pretty expensive to create those copies.
# So we should double-check if the copy is really needed.

"""Expensive Loops"""
# If you do an expensive operation inside a loop, you multiply the time it takes to do the expensive operation by
# the amount of times you repeat the loop.

# Whenever you have a loop in your code, make sure to check what actions you're doing, and see if there are operations
# you can take out of the loop to do them just once.

# Instead of making one network call for each element, make one call before the loop.
# Instead of reading from disk for each element, read the whole thing before the loop.
# Even if the operations done inside the loop aren't especially expensive, if we're going through a list of
# a thousand elements, and we only need five out of them, we're wasting time on elements we don't need.
# Make sure that the list of elements that you're iterating through is only as long as you really need it to be.

# Another thing to remember about loops is to break out of the loop once you found what you were looking for.
# In Python, we do this using the keyword 'break'.
# Breaking out of loops means that as soon as the data we're looking for is found, our script can continue.

# Say you're writing a script that checks if a given username is within the list of authorized entities, and if it is,
# it grants them access to a particular resource. You can use a 'for' loop to iterate through the list of entities.
# When the username is found, you can break out of the loop and continue the rest of the script.

# One last thing to keep in mind is that the right solution for one problem might not be right for a different problem.
# Say your service has a total of 20 users. In that case, it's okay to go over this list whenever you want to check
# something. It's short enough that you don't need to do any special optimization. But if your service has over a
# thousand users, you'll want to avoid going through that list unless absolutely necessary.
# If the service has hundreds of thousands of users, going through that list isn't even a possibility.
