"""Try-Except"""
# Returning None when something fails is a common pattern but not the only one.
# We could also decide to set a variable to some base value like 0 for numbers, empty str for strings,
# empty list for list, and so on.
# It all depends on what our function does and what we need to get that work done.
# The important point is that when we have an operation that might raise
# an error we want handle that failure gracefully by using the try-except block.
def character_frequency(filename):
    try:
        f = open(filename)
    except OSError:
        return None

    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters

# print(character_frequency(r'C:\pythonProject\Automation with Python\quiz_3_regex.py'))


"""Raising Errors"""
def validate_user(username, minlen):
    # This code works as long as the provided values are sensible. What would happen if the 'minlen' variable is 0 or
    # negative number? Our function will allow an empty username as valid which doesn't make much sense.
    # To prevent this from happening, we can add an extra check to our function which will verify the receipt parameters
    # are sane. In this case, returning false would be misleading because it's not necessarily that the username is
    # invalid but the provided 'minlen' value doesn't make sense. So let's add a check to verify
    # that 'minlen' is at least 1 and raise an error if that's not the case.
    if minlen < 1:
        raise ValueError('minlen must be at least 1')
    if len(username) < 3:
        return False
    if not username.isalnum():
        return False
    return True


# Let's look at an alternative to the raise keyword that we can use for situations where we want to check that our code
# behaves the way it should particularly when we want to avoid situations that should never happen.
# This is the 'assert' keyword. It tries to verify that a conditional expression is True,
# and if it's False it raises an AssertionError with the indicated message.
def validate_user(username, minlen):
    assert type(username) == str, 'username must be a string'
    if minlen < 1:
        raise ValueError('minlen must be at least 1')
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

# Assertions can be super helpful for debugging some code that's not behaving the way we expect it to.
# We can add them at any point where we want to ensure that the variables contain the values and types that they should
# or when we think that's something that shouldn't happen is happening.

# Note, Assertions will get removed from our code if we ask the interpreter to optimize it to run faster.
# As a rule, we should use raise to check for conditions that we expect to happen during normal execution of our code
# and assert to verify situations that aren't expected but that might cause our code to misbehave.

"""Testing for Expected Errors"""
# assert raises method provided by the unittest module




# Raise allows you to throw an exception at any time.
# https://docs.python.org/3/tutorial/errors.html#raising-exceptions
# Assert enables you to verify if a certain condition is met and throw an exception if it isn’t.
# https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement
# https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python
# The standard library documentation is kind of unclear. Basically `assert <something false>` will raise AssertionError, which the caller may need to handle.
# In the try clause, all statements are executed until an exception is encountered.
# https://docs.python.org/3/tutorial/errors.html#handling-exceptions
# Except is used to catch and handle the exception(s) that are encountered in the try clause.
# https://docs.python.org/3/library/exceptions.html#bltin-exceptions
# Other interesting Exception handling readings:
# https://doughellmann.com/posts/python-exception-handling-techniques/


