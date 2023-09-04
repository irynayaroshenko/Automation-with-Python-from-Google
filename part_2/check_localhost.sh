#!/usr/bin/env bash
# in video #!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
  echo "Everything ok"
else
  echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi


# We start with the if keyword followed by the grep command that we'll use to
  #check for success.
  #At the end of the command, we have a semicolon followed by the word then.
  #After that comes the body of the conditional, make sense?
  #We're using indentation like in Python.
  #This is a good style choice, and it makes the code more readable.
  #But it's not mandatory in Bash.
  #It's possible to write this in one line and
  #sometimes we might do that when the amount of code is small enough.
  #In general, though, it's nice to have commands in separate lines and
  #use indentation to clearly show the body of the conditional.
  #We also have an else block for when the command doesn't finish successfully.
  #And finally, our conditional block finishes using the 'fi' keyword (a backwards "if").
  #You can see how some things are the same as in Python.