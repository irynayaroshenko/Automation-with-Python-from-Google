import re


"""Capturing Groups
are portions of the pattern that are enclosed in parentheses.
Let's say that we have a list of people's full names which stored as last name, comma, first name.
We want to turn this around and create a string that starts with the first name followed by the last name.
We can do this using a regular expression with capturing groups.
First we'll create a matching pattern that matches a group of letters followed by
a comma, a space, and then another group of letters.
To capture our groups, we'll put each group of letters between parentheses. 
"""
result = re.search(r'^(\w*), (\w*)$', 'Yaroshenko, Ira')  # <re.Match object; span=(0, 15), match='Yaroshenko, Ira'>
print(result)
print(result.groups())  # ('Yaroshenko', 'Ira') As we defined 2 separate groups, the group method returns a tuple of 2 elements.
print(result.group())  # Yaroshenko, Ira
print(result.start())  # 0
print(result.end())  # 15

# Using indices: 0 - whole string, 1 - 1st group, 2 - 2nd group, etc.
print(result[0])  # Yaroshenko, Ira
print(result[1])  # Yaroshenko
print(result[2])  # Ira

# Construct desired format
print(f'{result[2]} {result[1]}')  # Ira Yaroshenko


def rearrange_name(name):
    # result = re.search(r'^(\w*), (\w*)$', name)  # 1st iteration
    # result = re.search(r'^(\w*), (\w*\s?[A-Z]?[.]?)$', name)  # my solution
    result = re.search(r'^([\w .-]*), ([\w .-]*)$', name)  # solution from video
    if result is None:
        return name
    return f'{result[2]} {result[1]}'


print(rearrange_name('Murloc, cat'))  # cat Murloc
print(rearrange_name('Hopper, Grace M.'))  # Hopper, Grace M. (1st iteration doesn't match cause \w doesn't match . and space)

"""More on Repetition Qualifiers"""
# basic: * + ?
# advanced: numeric repetition qualifiers: {}
print(re.search(r'[a-zA-z]{5}', 'a ghosts'))  # <re.Match object; span=(2, 7), match='ghost'> - exactly 5 letters
print(re.findall(r'[a-zA-Z]{5}', 'a scary ghost appeared'))  # ['scary', 'ghost', 'appea']
print(re.findall(r'\b[a-zA-Z]{5}\b', 'A scary ghost appeared'))  # ['scary', 'ghost'] - match only full words of 5 let-s

# if we wanted to match a range of five to ten letters or numbers
print(re.findall(r'\w{5,10}', 'I really like strawberries'))  # ['really', 'strawberri']
print(re.findall(r'\b\w{5,10}\b', 'I really like strawberries'))  # ['really']

# These ranges can also be open-ended.A number followed by a comma means at least that many repetitions with no upper
# boundary limited only by the maximum repetitions in the source text.
print(re.findall(r'\w{5,}', 'I really like strawberries'))  # ['really', 'strawberries']

# Here we look for a pattern that was an S followed by up to 20 alphanumeric characters.
# So we got a match for strawberries which starts with S, and is followed by 11 characters.
print(re.findall(r's\w{,20}', 'I really like strawberries'))  # ['strawberries']

# The long_words function returns all words that are at least 7 characters
def long_words(text):
    pattern = r'\w{7,}'
    result = re.findall(pattern, text)
    return result

# print(long_words("I like to drink coffee in the morning.")) # ['morning']
# print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
# print(long_words("I never drink tea late at night.")) # []

"""Extracting a PID (Process ID) Using regexes"""
# log = 'July 31 07:53:34 mycomputer bad_process[12345]: ERROR Performing package upgrade'  # 12345
# log = 'Another string with numbers [875087777]'  # <re.Match object; span=(28, 39), match='[875087777]'>

# error if str doesn't have a block of numbers between the square brackets, and we use index
log = '99 elephants in a [cage]'
regex = r'\[(\d+)\]'
result = re.search(regex, log)
print(result)  # None
# print(result[1])  # TypeError: 'NoneType' object is not subscriptable

# How to omit such error: We should have a function that extracts the process ID or PID when possible,
# and does something else if not.
# def extract_pid(log_line):
#     regex = r'\[(\d+)\]'
#     result = re.search(regex, log_line)
#     if result is None:
#         return 'No matches.'
#     return result[1]


# print(extract_pid(log))

# Add to the regular expression used in the extract_pid function, to return the uppercase message in parentheses,
# after the process id. r'^([\w .-]*), ([\w .-]*)$'

def extract_pid(log_line):
    regex = r"\[(\d+)\][: ]*([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)


"""Splitting and Replacing
split - works similarly to the split func that we used before with strings. But instead of taking a string as a separator,
you can take any regular expression as a separator. E.g., we may want to split a piece of text into separate sentences.
To do that we need to check not only for the dots but also for question marks or exclamation marks
since they're also valid sentence endings."""
# separators are not included
print(re.split(r'[.?!]', 'One sentence. Another one? And last one!'))  # ['One sentence', ' Another one', ' And last one', '']
# separators are included
print(re.split(r'([.?!])', 'One sentence. Another one? And last one!'))  # ['One sentence', '.', ' Another one', '?', ' And last one', '!', '']

# sub - is used for creating new strings by substituting all or part of them for a different string, similar to the
# replace string method but using regular expressions for both the matching and the replacing.
# example: some logs in our system that included users' e-mail addresses, and we wanted to anonymize the data by
# removing all the addresses
print(re.sub(r'[\w.%+-]+@[\w.-]+', '[REDACTED]', 'Received an e-mail for go_nut%+_.s36@my.ex-amp_le.com'))  # Received an e-mail for [REDACTED]

# example with switching names result = re.search(r'^(\w*), (\w*)$', 'Yaroshenko, Ira')
# Use \2 to indicate the second captured group followed by a space and \1 to indicate the first captured group.
result = re.sub(r'^([\w .-]*), ([\w .-]*)$', r'\2 \1', 'Yaroshenko, Ira')
print(result)  # Ira Yaroshenko

print(re.split(r"the|a", "One sentence. Another one? And the last one!"))  # ['One sentence. Ano', 'r one? And ', ' l', 'st one!']
