"""Advanced Bash Concepts

While Loops in Bash Scripts"""

# open while.sh

# When using while loops and bash scripts, it's common to have a loop that retries a command a number of times until it
# succeeds. This is useful with commands that use network connections or that access resources that might be locked.
# These commands can fail for external reasons, and they're likely to succeed after a retry or two.
# To simulate a command that sometimes succeeds or sometimes fails, we have a small Python script that will return
# an exit value picked at random by a range that we give it.
# open random-exit.py

# open retry.sh
# Here we're getting the value of a command line argument using the $1, this is what we use in Bash to
# access the first command line argument.
# In Python, we get the same information using sys.argv[1].
# So we store the parameter and the variable called command, and then we execute the while loop until either the command
# succeeds or the end variable reaches a value of 5.
# In other words, if the received command fails, we'll retry up to 5 times.
# In the body of the while loop, we first sleep a few seconds, then increment the variable and print the number of free
# try attempts.
# So why do we call the sleep command? - the idea here is that if the command we're calling is failing due to CPU usage,
# network or resource exhaustion, it might make sense to wait a bit before trying again.
# So the more we try, the more we wait.
# We need to let our computer catch a breather and recover from whatever is making our command fail.
# In our simulation, the command fails randomly but this retry script works with any other commands that could fail
# for a wide range of reasons.
# To try this out, we'll need to call our retry script with the random exit command as a parameter:
# ./retry.sh ./random-exit.py

# Result: open retry_script_result.png


"""For Loops in Bash Scripts"""
# In Bash, we construct for sequences just by listing the elements with spaces in between.
# open fruits.sh

# Imagine that you're migrating your company's website from one web server software to another.
# Your web content is stored in a bunch of files that all end in uppercase HTM, and the new software requires that
# they all end in lowercase html.
# open old_website_content.png

# basename
# takes a filename and an extension - returns the name without the extension, e.g.
# basename index.HTM .HTM => index

# open rename.sh
# Iterate with a for loop through all the files that end with.HTM. For each file call 'basename' to keep the part of
# the file and store that in a variable called 'name'. use $ and () to call the command and keep the output.

# "$file", "$name.html"
# Surround file variable with "" to allow the command to work even if the file has spaces in its name.
# It's a good practice in Bash scripts when dealing with file names or any variables that could include spaces.

# !! Tip !!
# Whenever you're going to run a script like this that modifies the files in your file system, it's a good idea to first
# run it without actually modifying the file system. This will catch any possible bugs that the script might have.
# So instead of just running it as it is right now, we'll add an echo in front of the mv command.
# This means that instead of actually renaming, our script we'll print the renaming that it plans to do.
# open test_rename_script.png

# When after testing you delete 'echo' from script and execute again it won't be printed anything, cause these commands
# don't print anything when they succeed.
# Note: don't forget change file mode before executing: chmod +x rename.sh

# Result of rename.sh: open rename_script _result.png
