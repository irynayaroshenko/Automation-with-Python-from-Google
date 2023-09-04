"""Finding Invalid Data"""
# watch https://www.youtube.com/watch?v=ElTzRbab7_s&list=PLP8aFdeDk9g4ImMVv0PwgTl7ztwBZryi0&index=13&pp=iAQB

# We have a program that reads data from a CSV file, processes it, and then imports it into a database.
# One of the users of the system tells us that the file they're trying to import fails with an obscure import error.
# They've sent us the file, so we can try it ourselves.
# To call the command, we'll connect the output of 'cat' contacts.csv, the file that the user sent us, to the import.py
# command.

# Remember, testing shouldn't be in production.
# And since this script is going to be trying to import data into a database, we should run it against the test
# database instead of the production database.
# To do that, we'll use the --server flag that takes the name of the database server (here, 'test') as the parameter:


# Using:
# cat contacts.csv | ./import.py --server test


# Output:
# Import error  (not much info for us)

# Check how big the file is:

# wc - counts characters, words, and lines in a file

# wc -l
# print the amount of line in the file


# Using:
# wc -l contacts.csv


# Output:
# 100 contacts.csv


# We can try passing only half of the file to the script and check if it succeeds or fails. Till we find exact line/-s.

# We can use 'head' command to print the first lines in the file, and 'tail' command to print the last lines.
# We can pass the amount of lines we want to include as a parameter, e.g. 'head -15' will print the first 15 lines,
# while 'tail -20' will print the last 20 lines. Open binary_search_problem_1.png

# head -15 contacts.csv
# tail -20 contacts.csv

# Our command reads the file to import from standard input. So we can use pipes to connect the output of our head or
# tail commands to it. Put first half of the file


# Using (Put first half of the file, first 50 lines):
# head -50 contacts.csv | ./import.py --server test

# Using (Put first quarter of the file, first 25 lines):
# head -50 contacts.csv | head -25 | ./import.py --server test

# Using (Check second quarter of the file to verify that the problem is there):
# head -50 contacts.csv | tail -25 | ./import.py --server test

# Continue splitting till you find the problem:

# head -50 contacts.csv | tail -25 | head -13 | ./import.py --server test
# head -50 contacts.csv | tail -25 | tail -12 | head -6 | ./import.py --server test
# head -50 contacts.csv | tail -25 | tail -12 | head -6 | head -3 | ./import.py --server test

# Print out left 3 to find the problem (open binary_search_problem_2.png):
# head -50 contacts.csv | tail -25 | tail -12 | head -6 | head -3

# This is a comma separated file which means that each comma is used as a separator between the fields in the file.
# If a field includes commas, it should be written between quotes ("P.O. Box 548, 5515 In Avenue").
# But in the case of the third line, we can see that there's a comma instead of a period after the middle initial, and
# this is not written between quotes (Rhona K, England).
# The importing script is then confused because there are too many fields in this line.
# Edit the file and fix it.
