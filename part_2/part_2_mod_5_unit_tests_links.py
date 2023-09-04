"""Unit tests"""
# open rearrange_test.py
import re


def rearrange_name(name):
    result = re.search(r'^([\w .]*), ([\w .]*)$', name)
    return f'{result[2], result[1]}'

# first, manually validate
print(rearrange_name('Yaroshenko, Iryna'))

# We'll check this by importing the function in an interpreter. To do that, we'll use a keyword 'from'
# from rearrange import rearrange_name (in video they imported from module and run via cmd)

"""Edge cases"""
# Remember that it's bad for automation to fail silently.
# Other kinds of edge cases usually include things like passing zero to a function that expects a number, or negative
# numbers, or extremely large numbers


# Best of Unit Testing Standard Library Module
# Understand a Basic Example:
# https://docs.python.org/3/library/unittest.html#basic-example
# Understand how to run the tests using the Command Line:
# https://docs.python.org/3/library/unittest.html#command-line-interface
# Understand various Unit Test Design Patterns:
# https://docs.python.org/3/library/unittest.html#organizing-test-code
# Understand the uses of setUp, tearDown; setUpModule and tearDownModule

# Understand more specific assertions such as assertRaises
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
