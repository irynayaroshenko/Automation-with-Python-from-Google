#!/usr/bin/env bash
# in video #!/bin/bash

n=1
while [ $n -le 5 ]; do
    echo "Iteration number $n"
    ((n+=1))  # bash construct of double parentheses allow do arithmetic operations with variables.
done