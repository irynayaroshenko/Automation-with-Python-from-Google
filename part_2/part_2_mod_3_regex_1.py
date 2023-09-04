import re


log = 'July 31 07:53:34 mycomputer bad_process[12345]: ERROR Performing package upgrade'
# Find with index
# index = log.index('[')
# print(index)
# print(log[index + 1: index + 6])

# Find with regex
regex = r'\[(\d+)\]'
result = re.search(regex, log)
print(result)  # <re.Match object; span=(39, 46), match='[12345]'>  span=(39, 46) - shows position in the string
print(result[1])

# grep command (Linux)
# grep is case sensative: grep thon home/user/folder
# to ignore case, use grep -i:
""" grep -i python /usr/share/dict/words """

# Reserved characters which give extra meaning
# Dot (.) means any character (is a wildcard which can be replaced by any char)
""" grep l.rts /usr/share/dict/words """

# ^ (caret or circumflex ) and $
# These tell us where in the line the regex should match from. The circumflex indicates the beginning
# and the dollar sign indicates the end of the line. One thing to remember is
# that the circumflex and the dollar sign specifically match the start and end of the line, not a string
""" grep ^fruit /usr/share/dict/words   returns: fruit, fruitcake,fruits, fruit's, etc.
    grep cat$ /usr/share/dict/words     returns: bobcat, cat, scat, Muscat, etc.
"""

result2 = re.search(r'aza', 'plaza')
print(result2)  # <re.Match object; span=(2, 5), match='aza'>
print(result2[0])  # aza

# Returns None if match was not found


print(re.search(r'^x', 'xena'))  # <re.Match object; span=(0, 1), match='x'>
print(re.search(r'obr$', 'xenaobr'))  # <re.Match object; span=(4, 7), match='obr'>
print(re.search(r'p.ng', 'penguin'))  # <re.Match object; span=(0, 4), match='peng'>
print(re.search(r'p.ng', 'sponge'))  # <re.Match object; span=(1, 5), match='pong'>


def check_aei(text):
    result = re.search(r"a.e.i", text)
    return result is not None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

# to ignorecase use re.IGNORECASE
print(re.search(r'p.ng', 'Pangaea', re.IGNORECASE))  # <re.Match object; span=(0, 4), match='Pang'>


"""Wildcards and Character Classes"""
# Character classes are written inside square brackets and let us list the characters we want to match inside
# those brackets.

# Match the word Python but allow for both lowercase or uppercase p.
print(re.search(r'[Pp]ython', 'Python'))  # <re.Match object; span=(0, 6), match='Python'>

# define range of characters (look string preceded by any lowercase letter)
print(re.search(r'[a-z]way', 'The end of the highway'))  # <re.Match object; span=(18, 22), match='hway'>
print(re.search(r'[a-z]way', 'What a way to go'))  # None - because 'way' is preceded by space not lower letter

# The same with [A-Z], [0-9]
print(re.search(r'cloud[a-zA-Z0-9]', 'cloudy'))  # <re.Match object; span=(0, 6), match='cloudy'>
print(re.search(r'cloud[a-zA-Z0-9]', 'cloud9'))  # <re.Match object; span=(0, 6), match='cloud9'>

# Fill in the code to check if the text passed contains punctuation symbols:
# commas, periods, colons, semicolons, question marks, and exclamation points.
def check_punctuation(text):
    result = re.search(r"[,.:;?!]", text)
    return result is not None


print(check_punctuation("This is a sentence that ends with a period."))  # True
print(check_punctuation("This is a sentence fragment without a period"))  # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!"))  # True
print(check_punctuation("End of the line"))  # False

# Sometimes we may want to match any characters that aren't in a group.
# To do that, we use a circumflex inside the square brackets. For example, let's create a search pattern that looks for
# any characters that's not a letter.
# Here matches a space character
print(re.search(r'[^a-zA-Z0-9]', 'This is a sentence with spaces.'))  # <re.Match object; span=(4, 5), match=' '>

# Here it matches the final dot in sentence as we added space to our regex
print(re.search(r'[^a-zA-Z0-9 ]', 'This is a sentence with spaces.'))  # <re.Match object; span=(30, 31), match='.'>

# If we want to match either one expression or another, we can use the pipe symbol (|) to do that.
# This lets us list alternative options that can get matched. For example, we could have an expression that matches
# either the word cat or the word dog, like this.
print(re.search(r'cat|dog', 'I like cats'))  # <re.Match object; span=(7, 10), match='cat'>

# Here we have both matches but get the first one
print(re.search(r'cat|dog', 'I like both dogs and cats'))  # <re.Match object; span=(12, 15), match='dog'>

# Use re.findall() to get all the matches
print(re.findall(r'cat|dog', 'I like both dogs and cats'))  # ['dog', 'cat']


""" Repetition Qualifiers (repeated matches) """
# .* - means that it matches any character repeated as many times as possible including zero.
# match Py followed by any number of other characters followed by n.
print(re.search(r'Py.*n', 'Pygmalion'))  # <re.Match object; span=(0, 9), match='Pygmalion'>

# In programming terms, we say that this behavior is greedy.
print(re.search(r'Py.*n', 'Python Programming'))  # <re.Match object; span=(0, 17), match='Python Programmin'>

# If we only wanted our patterns match letters, we should have used the character class instead like this.
# zero times is also a possibility
print(re.search(r'Py[a-z]*n', 'Python Programming'))  # <re.Match object; span=(0, 6), match='Python'>


# Egrep command includes 2 additional repetition qualifiers: + and ?
# + matches one or more occurrences of the character that comes before it.
print(re.search(r'o+l+', 'goldfish'))  # <re.Match object; span=(1, 3), match='ol'>
print(re.search(r'o+l+', 'woolly'))  # <re.Match object; span=(1, 5), match='ooll'>
print(re.search(r'o+l+', 'boil'))  # None


"""
The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least
twice. For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False. 
"""
def repeating_letter_a(text):
    result = re.search(r".*[Aa].*[Aa]", text)
    return result is not None


print(repeating_letter_a("banana"))  # True
print(repeating_letter_a("pineapple"))  # False
print(repeating_letter_a("Animal Kingdom"))  # True
print(repeating_letter_a("A is for apple"))  # True

# ? is another multiplier. It means either zero or one occurrence of the character before it.
# 'p' is optional as possible 0
print(re.search(r'p?each', 'To each their own'))  # <re.Match object; span=(3, 7), match='each'>
print(re.search(r'p?each', 'I like peaches'))  # <re.Match object; span=(7, 12), match='peach'>

