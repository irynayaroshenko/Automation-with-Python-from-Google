import re


# Escaping characters
print(re.search(r'\.com', 'google.com'))  # <re.Match object; span=(6, 10), match='.com'>

"""
When we see a pattern that includes a backslash, it could be escaping a special regex character or a special string
character.
Using raw strings, like we've been doing, helps avoid some of these possible confusion because the special characters
won't be interpreted when generating the string. They will only be interpreted when parsing the regular expression.
On top of this, Python also uses the backslash for a few special sequences that we can use to represent predefined
sets of characters.
\w matches any alphanumeric character including letters, numbers, and underscores.
\d for matching digits,
\s for matching whitespace characters like space, tab or new line,
\b for word boundaries
"""
print(re.search(r'\w*', 'This is an example'))  # <re.Match object; span=(0, 4), match='This'>
print(re.search(r'\w*', 'And_this_is_another'))  # <re.Match object; span=(0, 19), match='And_this_is_another'>


"""Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters
(including letters, numbers, and underscores) separated by one or more whitespace characters."""
def check_character_groups(text):
    result = re.search(r"\w+\s+\w+", text)
    return result is not None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

"""Match the pattern whole string"""
print(re.search(r'A.*a', 'Argentina'))  # <re.Match object; span=(0, 9), match='Argentina'>
print(re.search(r'A.*a', 'Azerbaijan'))  # <re.Match object; span=(0, 9), match='Azerbaija'>

# Thus, we need begin and end of line characters to make it clear that we only want to match
# lines that begin and end with the letter 'a'.
print(re.search(r'^A.*a$', 'Azerbaijan'))  # None

# To check if variable name is valid in Python (can contain any number of letters numbers or underscores,
# but it can't start with a number)
# Start with circumflex to indicate that we wanted to start from the beginning, and now a character class with
# all lowercase and uppercase letters plus the underscore. The rest of the variable can have
# as many numbers letters or underscores that we want. So we needed another character class this
# time containing numbers with a star at the end.
# One last thing, we want this to be the end of the string that we're matching.
# Otherwise, we could match something that could be a variable, but that also contains additional stuff after it.
# So we finish up with a dollar sign.
pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
print(re.search(pattern, '_is_this_valid'))  # <re.Match object; span=(0, 14), match='_is_this_valid'>
print(re.search(pattern, 'is_not valid'))  # None
print(re.search(pattern, '2not_with_num'))  # None
print(re.search(pattern, 'valid_with_num42'))  # <re.Match object; span=(0, 16), match='valid_with_num42'>

"""
Fill in the code to check if the text passed looks like a standard sentence: it starts with an uppercase letter,
followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point. 
"""
def check_sentence(text):
    result = re.search(r"^[A-Z][a-z ]+[.?!]$", text)
    return result is not None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
